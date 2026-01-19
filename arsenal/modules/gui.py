import time
import curses
import math
import json
import re
from curses import wrapper
from os.path import commonprefix, exists, isdir, expanduser, join
from os import sep
import glob

# local
from . import config
from . import command


class CheatslistMenu:
    globalcheats = []  # all cheats
    cheats = []  # cheats after search
    max_visible_cheats = 0
    input_buffer = ''
    position = 0
    page_position = 0

    xcursor = None
    x_init = None
    y_init = None

    @staticmethod
    def draw_prompt():
        """
        Create a prompt box
        at x : 0 / y : 5
        size 5 chars
        :return: the windows created
        """
        y, x = 5, 0
        ncols, nlines = 5, 1
        promptwin = curses.newwin(nlines, ncols, y, x)
        try:
            promptwin.addstr("\u2620  >", curses.color_pair(Gui.BASIC_COLOR))
        except:
            promptwin.addstr(">>>>", curses.color_pair(Gui.BASIC_COLOR))
        promptwin.refresh()
        return promptwin

    def draw_infobox(self):
        """
        Draw the top infobox (4 lines / width from param)
        :return: the window created
        """
        y, x = 0, 0
        ncols, nlines = self.width, 4
        infowin = curses.newwin(nlines, ncols, y, x)
        selected_cheat = self.selected_cheat()
        if selected_cheat is not None:
            infowin.addstr(y + 1, x + 2, Gui.draw_string(selected_cheat.name, self.width - 3),
                           curses.color_pair(Gui.INFO_NAME_COLOR))
            Gui.draw_highlighted_command(infowin, y + 2, x + 2, 
                                         selected_cheat.printable_command, self.width - 3)
        infowin.border()
        infowin.refresh()
        return infowin

    def draw_editbox(self):
        """
        Draw the edition box (in the right of the prompt box
        """
        y, x = 5, 6
        ncols, nlines = self.width - 5, 1
        editwin = curses.newwin(nlines, ncols, y, x)
        editwin.addstr(self.input_buffer, curses.color_pair(Gui.BASIC_COLOR))
        editwin.refresh()
        return editwin

    @staticmethod
    def draw_cheat(win, cheat, selected):
        """
        Draw a cheat line in the cheats list menu
        :param win:
        :param cheat:
        :param selected:
        """
        win_height, win_width = win.getmaxyx()
        prompt = '> '
        pin_indicator = 2
        max_width = win_width - len(prompt) - pin_indicator - len("\n")

        title = cheat.tags if cheat.tags != '' else cheat.str_title

        tags = cheat.get_tags()

        columns_list = ["title", "name", "description"]
        if Gui.with_tags:
            columns_list = ["tags"] + columns_list

        def get_col_size(max_width, ratio):
            """
            Return the column size from the given ratio

            :param max_width: The width maximal of the screen
            :param ratio: The ratio of the column
            """
            return math.floor((max_width * ratio) / 100)

        ratios = Gui.get_ratios_for_column(columns_list)

        columns = {"tags": {"width": get_col_size(max_width, ratios.get("tags", 0)),
                            "val": tags,
                            "color": Gui.COL4_COLOR_SELECT if selected else Gui.COL4_COLOR},
                   "title": {"width": get_col_size(max_width, ratios.get("title", 0)),
                             "val": cheat.str_title,
                             "color": Gui.COL3_COLOR_SELECT if selected else Gui.COL1_COLOR},
                   "name": {"width": get_col_size(max_width, ratios.get("name", 0)),
                            "val": cheat.name,
                            "color": Gui.COL2_COLOR_SELECT if selected else Gui.COL2_COLOR},
                   "description": {"width": get_col_size(max_width, ratios.get("description", 0)),
                                   "val": cheat.printable_command,
                                   "color": Gui.COL3_COLOR_SELECT if selected else Gui.COL3_COLOR}}

        cmd_key = cheat.str_title + cheat.name
        is_fav = Gui.is_favorite(cmd_key)

        if selected:
            win.addstr(prompt, curses.color_pair(Gui.CURSOR_COLOR_SELECT))
        else:
            win.addstr(' ' * len(prompt), curses.color_pair(Gui.BASIC_COLOR))

        if is_fav:
            win.addstr("* ", curses.color_pair(Gui.COL2_COLOR))
        else:
            win.addstr("  ", curses.color_pair(Gui.BASIC_COLOR))

        for column_name in columns_list:
            win.addstr("{:{}s}".format(Gui.draw_string(columns[column_name]["val"],
                                                       columns[column_name]["width"]),
                                       columns[column_name]["width"]),
                       curses.color_pair(columns[column_name]["color"]))
        win.addstr("\n")

    def draw_cheatslistbox(self):
        """
        Draw the box to show the cheats list
        """
        y, x = 6, 0
        ncols, nlines = self.width, self.height - 6
        listwin = curses.newwin(nlines, ncols, y, x)

        visible_cheats = self.cheats[self.page_position:self.max_visible_cheats + self.page_position]
        counter = self.page_position

        for cheat in visible_cheats:
            self.draw_cheat(listwin, cheat, counter == self.position)
            counter += 1

        listwin.refresh()

    def draw_footbox(self, info):
        """
        Draw the footer (number infos)
        :param info: str info to draw
        """
        y, x = self.height - 1, 0
        ncols, nlines = self.width, 1

        # print nb cmd info (bottom left)
        nbinfowin = curses.newwin(nlines, ncols, y, x)
        nbinfowin.addstr(info, curses.color_pair(Gui.BASIC_COLOR))
        nbinfowin.refresh()

        hotkey_hint = "[^E:Edit ^Y:Copy ^R:History ^F:Favorites ^P:Pin]"
        hint_x = (self.width - len(hotkey_hint)) // 2
        if hint_x > len(info) and self.width > 60:
            hintwin = curses.newwin(nlines, len(hotkey_hint) + 1, y, hint_x)
            hintwin.addstr(hotkey_hint, curses.color_pair(Gui.COL2_COLOR))
            hintwin.refresh()

    def match(self, cheat):
        """
        Function called by the iterator to verify if the cheatsheet match the entered values
        :param cheat: cheat to check
        :return: boolean
        """
        cmd_key = cheat.str_title + cheat.name

        if self.input_buffer.startswith('>') and not cheat.command.startswith('>'):
            return False

        if self.input_buffer == "!history":
            return cmd_key in Gui.command_history

        if self.input_buffer == "!fav":
            return Gui.is_favorite(cmd_key)

        for value in self.input_buffer.lower().split(' '):
            is_value_excluded = False
            if value.startswith("!") and len(value) > 1:
                value = value[1:]
                is_value_excluded = True

            if (value in cheat.str_title.lower()
                    or value in cheat.name.lower()
                    or value in cheat.tags.lower()
                    or value in "".join(cheat.command_tags.values()).lower()
                    or value in cheat.command.lower()):
                if is_value_excluded:
                    return False

            elif not is_value_excluded:
                return False
        return True

    def search(self):
        """
        Return the list of cheatsheet who match the searched term
        :return: list of cheatsheet to show
        """
        if self.input_buffer == "!history":
            history_order = {k: i for i, k in enumerate(Gui.command_history)}
            list_cheat = [c for c in self.globalcheats if (c.str_title + c.name) in history_order]
            list_cheat.sort(key=lambda c: history_order.get(c.str_title + c.name, 999))
            return list_cheat
        elif self.input_buffer != '':
            list_cheat = list(filter(self.match, self.globalcheats))
        else:
            list_cheat = self.globalcheats
        return list_cheat

    def selected_cheat(self):
        """
        Return the selected cheat in the list
        :return: selected cheat
        """
        if len(self.cheats) == 0:
            return None
        return self.cheats[self.position % len(self.cheats)]

    def draw(self, stdscr):
        """
        Draw the main menu to select a cheatsheet
        :param stdscr: screen
        """
        self.height, self.width = stdscr.getmaxyx()
        self.max_visible_cheats = self.height - 7
        # create prompt windows
        self.draw_prompt()
        # create info windows
        self.draw_infobox()
        # create cheatslist box
        self.draw_cheatslistbox()
        # draw footer
        info = "> %d / %d " % (self.position + 1, len(self.cheats))
        self.draw_footbox(info)
        # create edit windows
        self.draw_editbox()
        # init cursor position (if first draw)
        if self.x_init is None or self.y_init is None or self.xcursor is None:
            self.y_init, self.x_init = curses.getsyx()
            self.xcursor = self.x_init
        # set cursor position
        curses.setsyx(self.y_init, self.xcursor)
        curses.doupdate()

    def move_position(self, step):
        """
        :param step:
        """
        # SCROLL ?
        #
        # 0                                ---------      
        # 1                                |       |
        # 2                       ->   -----------------    <-- self.page_position
        # 3                      |     |   |       |   |       
        # 4 max_visible_cheats = |     |   |       |   |
        # 5                      |     |  >|xxxxxxx|   |    <-- self.position      
        # 6                      |     |   |       |   |       
        # 7                       ->   -----------------    <-- self.page_position+max_visible_cheats
        # 8                                |       |
        # 9                                ---------        <-- len(self.cheats)
        self.position += step

        # clean position
        if self.position < 0: self.position = 0
        if self.position >= len(self.cheats) - 1: self.position = len(self.cheats) - 1

        # move page view UP
        if self.page_position > self.position:
            self.page_position -= (self.page_position - self.position)

            # move page view DOWN
        if self.position >= (self.page_position + self.max_visible_cheats):
            self.page_position += 1 + (self.position - (self.page_position + self.max_visible_cheats))

    def move_page(self, step):
        """
        :param step:
        """
        # only move if it is possible
        if len(self.cheats) > self.max_visible_cheats:
            new_pos = self.page_position + step * self.max_visible_cheats
            # clean position
            if new_pos >= (len(self.cheats) + 1 - self.max_visible_cheats):
                self.position = len(self.cheats) - 1
                self.page_position = len(self.cheats) - self.max_visible_cheats
            elif new_pos < 0:
                self.position = self.page_position = 0
            else:
                self.position = self.page_position = new_pos

    def check_move_cursor(self, n):
        return self.x_init <= (self.xcursor + n) < self.x_init + len(self.input_buffer) + 1

    def run(self, stdscr):
        """
        Cheats selection menu processing..
        :param stdscr: screen
        """
        Gui.init_colors()
        Gui.load_history()
        Gui.load_favorites()
        stdscr.clear()
        self.height, self.width = stdscr.getmaxyx()
        self.max_visible_cheats = self.height - 7
        self.cursorpos = 0

        while True:
            stdscr.refresh()
            self.cheats = self.search()
            self.draw(stdscr)
            c = stdscr.getch()
            if c == curses.KEY_ENTER or c == 10 or c == 13:
                if self.selected_cheat() is not None:
                    cheat = self.selected_cheat()
                    cmd_key = cheat.str_title + cheat.name
                    Gui.add_to_history(cmd_key)
                    Gui.cmd = command.Command(cheat, Gui.arsenalGlobalVars)
                    args_menu = ArgslistMenu(self)
                    args_menu.run(stdscr)
                    stdscr.refresh()
                    break
            elif c == curses.KEY_F10 or c == 27:
                if Gui.confirm_exit(stdscr):
                    Gui.cmd = None
                    break
            elif c == 339 or c == curses.KEY_PPAGE:
                # Page UP
                self.move_page(-1)
            elif c == 338 or c == curses.KEY_NPAGE:
                # Page DOWN
                self.move_page(1)
            elif c == curses.KEY_UP:
                # Move UP
                self.move_position(-1)
            elif c == curses.KEY_DOWN:
                # Move DOWN
                self.move_position(1)
            elif c == curses.KEY_BACKSPACE or c == 127 or c == 8:
                if self.check_move_cursor(-1):
                    i = self.xcursor - self.x_init - 1
                    self.input_buffer = self.input_buffer[:i] + self.input_buffer[i + 1:]
                    self.xcursor -= 1
                    self.position = 0
                    self.page_position = 0
            elif c == curses.KEY_DC or c == 127:
                if self.check_move_cursor(1):
                    i = self.xcursor - self.x_init - 1
                    self.input_buffer = self.input_buffer[:i + 1] + self.input_buffer[i + 2:]
                    # new search -> reset position
                    self.position = 0
                    self.page_position = 0
            elif c == curses.KEY_LEFT:
                # Move cursor LEFT
                if self.check_move_cursor(-1): self.xcursor -= 1
            elif c == curses.KEY_RIGHT:
                # Move cursor RIGHT
                if self.check_move_cursor(1): self.xcursor += 1
            elif c == curses.KEY_BEG or c == curses.KEY_HOME:
                # Move cursor to the BEGIN
                self.xcursor = self.x_init
            elif c == curses.KEY_END:
                # Move cursor to the END
                self.xcursor = self.x_init + len(self.input_buffer)
            elif c == 9:
                # TAB cmd auto complete
                if self.input_buffer != "":
                    predictions = []
                    for cheat in self.cheats:
                        if cheat.command.startswith(self.input_buffer):
                            predictions.append(cheat.command)
                    if len(predictions) != 0:
                        self.input_buffer = commonprefix(predictions)
                        self.xcursor = self.x_init + len(self.input_buffer)
                        self.position = 0
                        self.page_position = 0
            elif c == 25:
                # Ctrl+Y: Copy selected command to clipboard
                if self.selected_cheat() is not None:
                    try:
                        import pyperclip
                        pyperclip.copy(self.selected_cheat().command)
                    except ImportError:
                        pass
            elif c == 16:
                # Ctrl+P: Toggle pin/favorite on selected command
                if self.selected_cheat() is not None:
                    cheat = self.selected_cheat()
                    cmd_key = cheat.str_title + cheat.name
                    Gui.toggle_favorite(cmd_key)
            elif c == 6:
                if self.input_buffer == "!fav":
                    self.input_buffer = ""
                else:
                    self.input_buffer = "!fav"
                self.position = 0
                self.page_position = 0
            elif c == 18:
                if self.input_buffer == "!history":
                    self.input_buffer = ""
                else:
                    self.input_buffer = "!history"
                self.position = 0
                self.page_position = 0
            elif c == 5:
                # Ctrl+E: Edit command directly
                if self.selected_cheat() is not None:
                    cheat = self.selected_cheat()
                    cmd_key = cheat.str_title + cheat.name
                    Gui.add_to_history(cmd_key)
                    Gui.cmd = command.Command(cheat, Gui.arsenalGlobalVars)
                    editor_menu = CommandEditorMenu(self)
                    editor_menu.cmd_buffer = cheat.command
                    editor_menu.run(stdscr)
                    stdscr.refresh()
                    if Gui.cmd is not None:
                        break
            elif 20 <= c < 127:
                i = self.xcursor - self.x_init
                self.input_buffer = self.input_buffer[:i] + chr(c) + self.input_buffer[i:]
                self.xcursor += 1
                # new search -> reset position
                self.position = 0
                self.page_position = 0


class ArgslistMenu:
    current_arg = 0
    max_preview_size = 0
    prev_lastline_len = 0

    # init arg box margins
    AB_TOP = 0
    AB_SIDE = 0

    xcursor = None
    x_init = None
    y_init = None

    def __init__(self, prev):
        self.previous_menu = prev

    def get_nb_preview_new_lines(self):
        """
        Returns the number of preview lines
        :return:
        """
        next_arg = 0
        nblines = 0
        multiline = '\n' in Gui.cmd.cmdline
        firstline = True
        parts = Gui.cmd.get_command_parts()
        nb_args_todo = len(parts) - 1
        # in case of multiline cmd process each line separately
        # for each line we have to count each char and deduce the
        # number of lines needed to print it
        for line in Gui.cmd.cmdline.split('\n'):
            nbchar = 0

            # for all lines except the first one we have ' >' in addition
            if multiline and (not firstline):
                nbchar = 2
            else:
                firstline = False

            # extract len of args in the current line
            i = 0
            for arg_name, arg_val in Gui.cmd.args:
                if i == next_arg and nb_args_todo > 0:
                    if arg_val != "":
                        # use value len if not empty
                        nbchar += len(arg_val)
                    else:
                        # else use name len + 2 for '<' and '>'
                        nbchar += (len(arg_name) + 2)
                    next_arg += 1
                    nb_args_todo -= 1
                i += 1

            # len of the cmd body
            for p in parts:
                nbchar += len(p)

            nblines += 1 + ((nbchar - 1) // self.max_preview_size)

        return nblines - 1

    def next_arg(self):
        """
        Select the next argument in the list
        """
        # reset cursor position
        self.xcursor = None
        self.x_init = None
        self.y_init = None
        # change selected arg
        if self.current_arg < Gui.cmd.nb_args - 1:
            self.current_arg += 1
        else:
            self.current_arg = 0

    def previous_arg(self):
        """
        Select the previous argument in the list
        """
        # reset cursor position
        self.xcursor = None
        self.x_init = None
        self.y_init = None
        # change selected arg
        if self.current_arg > 0:
            self.current_arg -= 1
        else:
            self.current_arg = Gui.cmd.nb_args - 1

    def draw_preview_part(self, win, text, color):
        """
        Print a part of the preview cmd line
        And start a new line if the last line of the preview is too long
        :param win: window
        :param text: part of the preview to draw
        :param color: color used to draw the text
        """
        for c in text:
            if c == "\n":
                # multi line cmd -> new line
                self.prev_lastline_len = 2
                win.addstr("\n    > ", color)
            elif self.prev_lastline_len < self.max_preview_size:
                # size ok -> print the char
                self.prev_lastline_len += 1
                win.addstr(c, color)
            else:
                # last line too long -> new line
                self.prev_lastline_len = 1
                win.addstr("\n    " + c, color)

    def draw_selected_arg(self, y_pos):
        """
        Draw the selected argument line in the argument menu
        """
        y, x = self.AB_TOP + y_pos + self.current_arg, self.AB_SIDE + 1
        ncols, nlines = self.width - 2 * (self.AB_SIDE + 1), 1
        arg = Gui.cmd.args[self.current_arg]
        max_size = self.max_preview_size - 4 - len(arg[0])
        selectedargline = curses.newwin(nlines, ncols, y, x)
        selectedargline.addstr("   > ", curses.color_pair(Gui.BASIC_COLOR))
        selectedargline.addstr(arg[0], curses.color_pair(Gui.ARG_NAME_COLOR))
        selectedargline.addstr(" = " + Gui.draw_string(arg[1], max_size), curses.color_pair(Gui.BASIC_COLOR))
        selectedargline.refresh()

    def draw_args_list(self, y_pos):
        """
        Draw the asked arguments list in the argument menu
        """
        y, x = self.AB_TOP + y_pos, self.AB_SIDE + 1
        ncols, nlines = self.width - 2 * (self.AB_SIDE + 1), Gui.cmd.nb_args + 1
        argwin = curses.newwin(nlines, ncols, y, x)
        for arg in Gui.cmd.args:
            max_size = self.max_preview_size + 4
            argline = Gui.draw_string("     {} = {}".format(*arg), max_size) + "\n"
            argwin.addstr(argline, curses.color_pair(Gui.BASIC_COLOR))
        argwin.refresh()

    def draw_desc_preview(self, argprev, p_x, p_y, description_lines):
        """
        Draw the descriptions_line preview in the preview windows (argprev)
        """
        # draw description
        if len(description_lines) > 0:
            argprev.addstr(p_y, p_x, "-----", curses.color_pair(Gui.BASIC_COLOR))
            p_y += 1
            for description_line in description_lines:
                argprev.addstr(p_y, p_x, description_line, curses.color_pair(Gui.BASIC_COLOR))
                p_y += 1
            p_y += 1
            argprev.refresh()
        return p_y

    def draw_cmd_preview(self, argprev, p_x, p_y=1):
        """
        Draw the cmd preview in the argument menu
        Also used to draw the borders of this menu
        """
        cmdparts = Gui.cmd.get_command_parts()

        # draw command
        argprev.addstr(p_y, p_x, "$ ", curses.color_pair(Gui.BASIC_COLOR))

        # draw preview cmdline
        for i in range(len(cmdparts) + Gui.cmd.nb_args):
            if i % 2 == 0:
                # draw cmd parts in white
                self.draw_preview_part(argprev, cmdparts[i // 2], curses.color_pair(Gui.BASIC_COLOR))
            else:
                # get argument value
                if Gui.cmd.args[(i - 1) // 2][1] == "":
                    # if arg empty use its name
                    arg = '<' + Gui.cmd.args[(i - 1) // 2][0] + '>'
                else:
                    # else its value
                    arg = Gui.cmd.args[(i - 1) // 2][1]

                # draw argument
                if (i - 1) // 2 == self.current_arg:
                    # if arg is selected print in blue
                    self.draw_preview_part(argprev, arg, curses.color_pair(Gui.ARG_NAME_COLOR))
                else:
                    # else in white
                    self.draw_preview_part(argprev, arg, curses.color_pair(Gui.BASIC_COLOR))
        argprev.border()
        argprev.refresh()

    def draw(self, stdscr):
        """
        Draw the arguments menu to ask them
        :param stdscr: screen
        """
        # init vars and set margins values
        self.height, self.width = stdscr.getmaxyx()
        self.AB_SIDE = 5
        padding_text_border = 3
        self.max_preview_size = self.width - (2 * self.AB_SIDE) - (2 * padding_text_border)

        # draw background cheatslist menu (clean resize)
        self.previous_menu.draw(stdscr)

        # draw argslist menu popup
        self.prev_lastline_len = 0
        nbpreviewnewlines = self.get_nb_preview_new_lines()
        # if Gui.cmd.nb_args != 0:
        #     nbpreviewnewlines = self.get_nb_preview_new_lines()
        # else:
        #     nbpreviewnewlines = 0

        # -------------- border
        # cmd
        # nbpreviewnewlines
        # .............. args margin top
        # args
        # ------
        # description
        # .............  description margin
        # ---------- border

        # width - preview
        ncols = self.width - 2 * self.AB_SIDE

        # prepare showed description
        description_lines = Gui.cmd.get_description_cut_by_size(ncols - (padding_text_border * 2))

        border_height = 1
        cmd_height = 1 + nbpreviewnewlines
        args_height = (2 + Gui.cmd.nb_args) if (Gui.cmd.nb_args > 0) else 0
        desc_height = (len(description_lines) + 1 + 1) if (len(description_lines) > 0) else 0
        hint_height = 1

        cmd_pos = 1
        args_pos = border_height + cmd_height + 1
        desc_pos = args_pos + args_height - 1

        nlines = border_height * 2 + cmd_height + args_height + desc_height + hint_height
        if nlines > self.height:
            nlines = self.height

        self.AB_TOP = (self.height - nlines) // 2
        y, x = self.AB_TOP, self.AB_SIDE

        try:
            argprev = curses.newwin(nlines, ncols, y, x)

            # draw command
            self.draw_cmd_preview(argprev, padding_text_border, cmd_pos)

            # draw description
            self.draw_desc_preview(argprev, padding_text_border, desc_pos, description_lines)

            hint = "[^E:Edit cmd] [^Y:Copy]"
            hint_y = nlines - 2
            hint_x = ncols - len(hint) - padding_text_border
            argprev.addstr(hint_y, hint_x, hint, curses.color_pair(Gui.COL2_COLOR))
            argprev.refresh()

            if len(Gui.cmd.args) > 0:
                self.draw_args_list(args_pos)
                self.draw_selected_arg(args_pos)
                # init cursor position (if first draw)
                if self.x_init is None or self.y_init is None or self.xcursor is None:
                    self.y_init, self.x_init = curses.getsyx()
                    # prefill compatibility
                    self.x_init -= len(Gui.cmd.args[self.current_arg][1])
                    self.xcursor = self.x_init + len(Gui.cmd.args[self.current_arg][1])
                # set cursor position
                curses.setsyx(self.y_init, self.xcursor)
                curses.doupdate()
        except curses.error:
            # catch all curses error to not end with an exception in case of size error
            pass

    def check_move_cursor(self, n):
        if Gui.cmd.nb_args == 0:
            return False
        return self.x_init <= (self.xcursor + n) < self.x_init + len(Gui.cmd.args[self.current_arg][1]) + 1

    def autocomplete_arg(self):
        """
        Autocomplete the current argument
        """
        # current argument value
        argument = Gui.cmd.args[self.current_arg][1]
        # look for all files that match the argument in the working directory
        matches = glob.glob('{}*'.format(argument))

        if not matches:
            return False

        # init the autocompleted argument
        autocompleted_argument = ""
        # autocompleted argument is the longest start common string in all matches
        for i in range(len(min(matches))):
            if not all(min(matches)[:i + 1] == match[:i + 1] for match in matches):
                break
            autocompleted_argument = min(matches)[:i + 1]

        # add a "/" at the end of the autocompleted argument if it is a directory
        if isdir(autocompleted_argument) and autocompleted_argument[-1] != sep:
            autocompleted_argument = autocompleted_argument + sep

        # autocomplete the argument 
        Gui.cmd.args[self.current_arg][1] = autocompleted_argument
        # update cursor position
        self.xcursor = self.x_init + len(autocompleted_argument)

    def run(self, stdscr):
        """
        Arguments selection menu processing..
        :param stdscr: screen
        """
        # init
        Gui.init_colors()
        stdscr.clear()
        while True:
            stdscr.refresh()
            self.draw(stdscr)
            c = stdscr.getch()
            if c == curses.KEY_ENTER or c == 10 or c == 13:
                if Gui.cmd.build():
                    break
            elif c == 5:
                # Ctrl+E: Edit command directly
                Gui.cmd.build()
                editor_menu = CommandEditorMenu(self.previous_menu)
                editor_menu.cmd_buffer = Gui.cmd.cmdline
                editor_menu.run(stdscr)
                stdscr.refresh()
                if Gui.cmd is not None:
                    break
            elif c == curses.KEY_F10 or c == 27:
                # exit args_menu -> return to cheatslist_menu
                self.previous_menu.run(stdscr)
                stdscr.refresh()
                break
            elif c == curses.KEY_DOWN:
                self.next_arg()
            elif c == curses.KEY_UP:
                self.previous_arg()
            elif c == 9:
                if Gui.cmd.args:
                    # autocomplete the current argument
                    if Gui.cmd.args[self.current_arg][1]:
                        self.autocomplete_arg()
                    # go to the next argument
                    else:
                        self.next_arg()
            elif c == 20:
                try:
                    from pyfzf.pyfzf import FzfPrompt
                    files = []
                    for fuzz_dir in config.FUZZING_DIRS:
                        files += glob.glob(fuzz_dir, recursive=True)
                    fzf = FzfPrompt().prompt(files)
                    # autocomplete the argument 
                    Gui.cmd.args[self.current_arg][1] = fzf[0]
                    # update cursor position
                    self.xcursor = self.x_init + len(fzf[0])
                except ImportError:
                    pass
            elif c == 25:
                # Ctrl+Y: Copy command to clipboard
                if Gui.cmd.build():
                    try:
                        import pyperclip
                        pyperclip.copy(Gui.cmd.cmdline)
                    except ImportError:
                        pass
            elif c == curses.KEY_BACKSPACE or c == 127 or c == 8:
                if self.check_move_cursor(-1):
                    i = self.xcursor - self.x_init - 1
                    Gui.cmd.args[self.current_arg][1] = Gui.cmd.args[self.current_arg][1][:i] + \
                                                        Gui.cmd.args[self.current_arg][1][i + 1:]
                    self.xcursor -= 1
            elif c == curses.KEY_DC or c == 127:
                # DELETE key
                if self.check_move_cursor(1):
                    i = self.xcursor - self.x_init - 1
                    Gui.cmd.args[self.current_arg][1] = Gui.cmd.args[self.current_arg][1][:i + 1] + \
                                                        Gui.cmd.args[self.current_arg][1][i + 2:]
            elif c == curses.KEY_LEFT:
                # Move cursor LEFT
                if self.check_move_cursor(-1): self.xcursor -= 1
            elif c == curses.KEY_RIGHT:
                # Move cursor RIGHT
                if self.check_move_cursor(1): self.xcursor += 1
            elif c == curses.KEY_BEG or c == curses.KEY_HOME:
                # Move cursor to the BEGIN
                self.xcursor = self.x_init
            elif c == curses.KEY_END:
                # Move cursor to the END
                self.xcursor = self.x_init + len(Gui.cmd.args[self.current_arg][1])
            elif 20 <= c < 127 and Gui.cmd.nb_args > 0:
                i = self.xcursor - self.x_init
                Gui.cmd.args[self.current_arg][1] = Gui.cmd.args[self.current_arg][1][:i] + chr(c) + \
                                                    Gui.cmd.args[self.current_arg][1][i:]
                self.xcursor += 1


class CommandEditorMenu:
    """
    Menu for directly editing the full command text
    """
    AB_TOP = 0
    AB_SIDE = 0

    xcursor = None
    x_init = None
    y_init = None

    def __init__(self, prev):
        self.previous_menu = prev
        self.cmd_buffer = ""
        self.scroll_offset = 0

    def draw(self, stdscr):
        """
        Draw the command editor popup
        """
        self.height, self.width = stdscr.getmaxyx()
        self.AB_SIDE = 3
        padding = 2

        # Draw background cheatslist menu
        self.previous_menu.draw(stdscr)

        # Calculate editor dimensions
        edit_width = self.width - 2 * self.AB_SIDE
        edit_height = 7
        self.max_cmd_width = edit_width - 2 * padding - 4  # 4 for "$ " prefix and borders

        self.AB_TOP = (self.height - edit_height) // 2
        y, x = self.AB_TOP, self.AB_SIDE

        try:
            editwin = curses.newwin(edit_height, edit_width, y, x)
            editwin.border()

            # Title
            title = " Edit Command (Enter: confirm, Esc: cancel) "
            title_x = (edit_width - len(title)) // 2
            editwin.addstr(0, title_x, title, curses.color_pair(Gui.INFO_NAME_COLOR))

            # Command prompt
            editwin.addstr(2, padding, "$ ", curses.color_pair(Gui.BASIC_COLOR))

            # Display command with scrolling if needed
            visible_cmd = self.cmd_buffer
            if len(self.cmd_buffer) > self.max_cmd_width:
                # Calculate visible portion based on cursor position
                cursor_pos = self.xcursor - self.x_init if self.xcursor and self.x_init else len(self.cmd_buffer)
                if cursor_pos > self.max_cmd_width - 5:
                    self.scroll_offset = cursor_pos - self.max_cmd_width + 5
                else:
                    self.scroll_offset = 0
                visible_cmd = self.cmd_buffer[self.scroll_offset:self.scroll_offset + self.max_cmd_width]
                if self.scroll_offset > 0:
                    visible_cmd = "<" + visible_cmd[1:]

            editwin.addstr(2, padding + 2, visible_cmd, curses.color_pair(Gui.BASIC_COLOR))

            # Hint
            hint = "[Ctrl+U: clear] [Ctrl+Y: copy]"
            editwin.addstr(4, padding, hint, curses.color_pair(Gui.COL2_COLOR))

            editwin.refresh()

            # Set cursor position
            if self.x_init is None or self.y_init is None or self.xcursor is None:
                self.y_init = y + 2
                self.x_init = x + padding + 2
                self.xcursor = self.x_init + len(self.cmd_buffer) - self.scroll_offset

            # Adjust cursor for scroll
            visible_cursor = self.x_init + (self.xcursor - self.x_init) - self.scroll_offset
            if visible_cursor < self.x_init:
                visible_cursor = self.x_init
            if visible_cursor > self.x_init + self.max_cmd_width:
                visible_cursor = self.x_init + self.max_cmd_width

            curses.setsyx(self.y_init, visible_cursor)
            curses.doupdate()

        except curses.error:
            pass

    def check_move_cursor(self, n):
        return self.x_init <= (self.xcursor + n) <= self.x_init + len(self.cmd_buffer)

    def run(self, stdscr):
        """
        Command editor processing
        """
        Gui.init_colors()
        stdscr.clear()

        while True:
            stdscr.refresh()
            self.draw(stdscr)
            c = stdscr.getch()

            if c == curses.KEY_ENTER or c == 10 or c == 13:
                # Confirm - set the edited command
                Gui.cmd.cmdline = self.cmd_buffer
                Gui.cmd.args = []
                Gui.cmd.nb_args = 0
                break

            elif c == curses.KEY_F10 or c == 27:
                # Cancel - return to cheatslist menu
                Gui.cmd = None
                self.previous_menu.run(stdscr)
                stdscr.refresh()
                break

            elif c == curses.KEY_BACKSPACE or c == 127 or c == 8:
                if self.check_move_cursor(-1):
                    i = self.xcursor - self.x_init - 1
                    self.cmd_buffer = self.cmd_buffer[:i] + self.cmd_buffer[i + 1:]
                    self.xcursor -= 1

            elif c == curses.KEY_DC:
                # DELETE key
                if self.xcursor - self.x_init < len(self.cmd_buffer):
                    i = self.xcursor - self.x_init
                    self.cmd_buffer = self.cmd_buffer[:i] + self.cmd_buffer[i + 1:]

            elif c == curses.KEY_LEFT:
                if self.check_move_cursor(-1):
                    self.xcursor -= 1

            elif c == curses.KEY_RIGHT:
                if self.check_move_cursor(1):
                    self.xcursor += 1

            elif c == curses.KEY_HOME or c == curses.KEY_BEG:
                self.xcursor = self.x_init

            elif c == curses.KEY_END:
                self.xcursor = self.x_init + len(self.cmd_buffer)

            elif c == 21:
                # Ctrl+U: clear line
                self.cmd_buffer = ""
                self.xcursor = self.x_init
                self.scroll_offset = 0

            elif c == 25:
                # Ctrl+Y: Copy to clipboard
                try:
                    import pyperclip
                    pyperclip.copy(self.cmd_buffer)
                except ImportError:
                    pass

            elif 32 <= c < 127:
                # Printable characters
                i = self.xcursor - self.x_init
                self.cmd_buffer = self.cmd_buffer[:i] + chr(c) + self.cmd_buffer[i:]
                self.xcursor += 1


class TmuxPaneSelectorMenu:
    """
    Menu for selecting which tmux pane/window to send the command to
    """
    def __init__(self, prev, panes_info, current_pane_id=None, current_window_index=None):
        """
        :param prev: previous menu for background drawing
        :param panes_info: list of dicts with pane info: 
                          [{'pane_id': str, 'window_name': str, 'pane_index': int, 
                            'window_index': int, 'current_path': str, 'is_current': bool}]
        :param current_pane_id: the pane where arsenal is running (to exclude/mark)
        :param current_window_index: the window index where arsenal is running
        """
        self.previous_menu = prev
        self.current_pane_id = current_pane_id
        self.current_window_index = current_window_index
        self.position = 0
        self.selected_pane = None
        
        other_panes = [p for p in panes_info if p['pane_id'] != current_pane_id]
        
        same_window_panes = [p for p in other_panes if p['window_index'] == current_window_index]
        other_window_panes = [p for p in other_panes if p['window_index'] != current_window_index]
        
        self.options = []
        
        for p in same_window_panes:
            self.options.append({'type': 'pane', 'pane_info': p, 'pane': p['pane']})
        
        for p in other_window_panes:
            self.options.append({'type': 'pane', 'pane_info': p, 'pane': p['pane']})

    def draw(self, stdscr):
        """
        Draw the pane selector popup
        """
        height, width = stdscr.getmaxyx()
        
        self.previous_menu.draw(stdscr)
        
        popup_width = min(width - 6, 70)
        popup_height = min(len(self.options) + 6, height - 4)
        
        top = (height - popup_height) // 2
        left = (width - popup_width) // 2
        
        try:
            popup = curses.newwin(popup_height, popup_width, top, left)
            popup.border()
            
            title = " Select Target Pane (Enter: select, Esc: cancel) "
            title_x = max(1, (popup_width - len(title)) // 2)
            popup.addstr(0, title_x, title[:popup_width-2], curses.color_pair(Gui.INFO_NAME_COLOR))
            
            header = "  {:10} {:3} {:12} {:4} {}".format("Session", "Win", "Window Name", "Pane", "Path")
            popup.addstr(2, 2, header[:popup_width-4], curses.color_pair(Gui.COL2_COLOR))
            
            max_visible = popup_height - 5
            visible_options = self.options[:max_visible]
            
            for i, opt in enumerate(visible_options):
                y = 3 + i
                if y >= popup_height - 2:
                    break
                
                pane = opt['pane_info']
                sess_name = pane.get('session_name', '?')[:10]
                win_idx = str(pane.get('window_index', '?'))
                win_name = pane.get('window_name', 'unnamed')[:12]
                pane_idx = str(pane.get('pane_index', '?'))
                path = pane.get('current_path', '')
                if len(path) > popup_width - 45:
                    path = "..." + path[-(popup_width - 48):]
                line = "{:10} {:3} {:12} {:4} {}".format(sess_name, win_idx, win_name, pane_idx, path)
                
                if i == self.position:
                    popup.addstr(y, 2, "> ", curses.color_pair(Gui.CURSOR_COLOR_SELECT))
                    popup.addstr(y, 4, line[:popup_width-6], curses.color_pair(Gui.COL1_COLOR_SELECT))
                else:
                    popup.addstr(y, 2, "  ", curses.color_pair(Gui.BASIC_COLOR))
                    popup.addstr(y, 4, line[:popup_width-6], curses.color_pair(Gui.BASIC_COLOR))
            
            hint = "[s: new sub-pane] [p: new pane]"
            hint_y = popup_height - 2
            hint_x = popup_width - len(hint) - 2
            if hint_x > 2:
                popup.addstr(hint_y, hint_x, hint, curses.color_pair(Gui.COL2_COLOR))
            
            popup.refresh()
            
        except curses.error:
            pass

    def run(self, stdscr):
        """
        Run the pane selector
        Returns: selected pane dict or None if cancelled, or 'new' for new pane
        """
        Gui.init_colors()
        
        while True:
            stdscr.refresh()
            self.draw(stdscr)
            c = stdscr.getch()
            
            if c == curses.KEY_ENTER or c == 10 or c == 13:
                if self.options:
                    selected = self.options[self.position]
                    return {'pane': selected['pane'], 'pane_info': selected.get('pane_info')}
                return None
                
            elif c == curses.KEY_F10 or c == 27:
                return None
                
            elif c == curses.KEY_UP:
                if self.position > 0:
                    self.position -= 1
                    
            elif c == curses.KEY_DOWN:
                if self.position < len(self.options) - 1:
                    self.position += 1
                    
            elif c == ord('s') or c == ord('S'):
                return 'new_subpane'
                
            elif c == ord('p') or c == ord('P'):
                return 'new_pane'


class Gui:
    # result CMD
    cmd = None
    arsenalGlobalVars = {}
    savefile = config.savevarfile
    # colors
    BASIC_COLOR = 0  # output std
    COL1_COLOR = 7
    COL2_COLOR = 4  # gold
    COL3_COLOR = 14  # purple light 
    COL4_COLOR = 5  # 26  # violet clair: 14  # 4 yellow  # 6 purple # 7 cyan # 9 dark grey
    COL5_COLOR = 5  # blue
    COL1_COLOR_SELECT = 256  # output std invert
    COL2_COLOR_SELECT = 256
    COL3_COLOR_SELECT = 256
    COL4_COLOR_SELECT = 256
    CURSOR_COLOR_SELECT = 266  # background red
    PROMPT_COLOR = 0
    INFO_NAME_COLOR = 4  # 5
    INFO_DESC_COLOR = 0
    INFO_CMD_COLOR = 0
    ARG_NAME_COLOR = 5
    # syntax highlighting colors
    SYN_PIPE_COLOR = 2  # green
    SYN_REDIRECT_COLOR = 3  # yellow/orange
    SYN_ARG_COLOR = 6  # cyan
    SYN_FLAG_COLOR = 5  # magenta
    SYN_VAR_COLOR = 4  # gold
    loaded_menu = False
    with_tags = False
    command_history = []
    favorites = set()

    DEFAULT_RATIOS = {"tags": 14, "title": 8, "name": 23, "description": 55}

    def __init__(self):
        self.cheats_menu = None

    @staticmethod
    def _get_history_file():
        return getattr(config, 'historyfile', join(expanduser("~"), ".arsenal_history.json"))

    @staticmethod
    def _get_favorites_file():
        return getattr(config, 'favoritesfile', join(expanduser("~"), ".arsenal_favorites.json"))

    @staticmethod
    def _get_max_history():
        return getattr(config, 'MAX_HISTORY_SIZE', 50)

    @staticmethod
    def load_history():
        histfile = Gui._get_history_file()
        if exists(histfile):
            with open(histfile, 'r') as f:
                Gui.command_history = json.load(f)

    @staticmethod
    def save_history():
        with open(Gui._get_history_file(), 'w') as f:
            json.dump(Gui.command_history[:Gui._get_max_history()], f)

    @staticmethod
    def add_to_history(cmd_key):
        if cmd_key in Gui.command_history:
            Gui.command_history.remove(cmd_key)
        Gui.command_history.insert(0, cmd_key)
        Gui.command_history = Gui.command_history[:Gui._get_max_history()]
        Gui.save_history()

    @staticmethod
    def load_favorites():
        favfile = Gui._get_favorites_file()
        if exists(favfile):
            with open(favfile, 'r') as f:
                Gui.favorites = set(json.load(f))

    @staticmethod
    def save_favorites():
        with open(Gui._get_favorites_file(), 'w') as f:
            json.dump(list(Gui.favorites), f)

    @staticmethod
    def toggle_favorite(cmd_key):
        if cmd_key in Gui.favorites:
            Gui.favorites.remove(cmd_key)
        else:
            Gui.favorites.add(cmd_key)
        Gui.save_favorites()

    @staticmethod
    def is_favorite(cmd_key):
        return cmd_key in Gui.favorites

    @staticmethod
    def init_colors():
        """ Init curses colors """
        curses.start_color()
        curses.use_default_colors()
        for i in range(0, 255):
            curses.init_pair(i + 1, i, -1)

    @classmethod
    def get_ratios_for_column(cls, columns_in_use):
        """
        Calculate the column size from the column to print

        :param columns_in_use: List of the column to print when drawing
        :return: The updated ratios size of each columns
        """
        missing_ratio = 0
        for col in cls.DEFAULT_RATIOS.keys():
            if col not in columns_in_use:
                missing_ratio += cls.DEFAULT_RATIOS.get(col)
        if not missing_ratio:
            return cls.DEFAULT_RATIOS

        new_ratio = {}
        for column in columns_in_use:
            new_ratio[column] = math.floor(cls.DEFAULT_RATIOS[column] + missing_ratio / len(columns_in_use))
        return new_ratio

    @staticmethod
    def draw_string(str_value, max_size):
        """
        Return a string of the max size, ended with ... if >= max_size
        :param str_value:
        :param max_size:
        :return:
        """
        result_string = str_value
        if len(str_value) >= max_size:
            result_string = str_value[:max_size - 4] + '...'
        return result_string

    @staticmethod
    def confirm_exit(stdscr):
        height, width = stdscr.getmaxyx()
        msg = "Exit Arsenal? [Y/n]"
        box_width = len(msg) + 4
        box_height = 3
        y = (height - box_height) // 2
        x = (width - box_width) // 2

        confirm_win = curses.newwin(box_height, box_width, y, x)
        confirm_win.border()
        confirm_win.addstr(1, 2, msg, curses.color_pair(Gui.INFO_NAME_COLOR))
        confirm_win.refresh()

        while True:
            c = stdscr.getch()
            if c in (ord('y'), ord('Y'), curses.KEY_ENTER, 10, 13):
                return True
            elif c in (ord('n'), ord('N'), 27):
                return False

    @staticmethod
    def draw_highlighted_command(win, y, x, cmd_str, max_width):
        pos = x
        i = 0
        tokens = re.split(r'(\||&&|;|>|>>|<|2>&1|\$\([^)]+\)|\$\{[^}]+\}|\$\w+|<[^>]+>|-{1,2}\w+)', cmd_str)
        for token in tokens:
            if pos - x >= max_width - 3:
                break
            remaining = max_width - (pos - x) - 3
            if remaining <= 0:
                break
            display_token = token[:remaining] if len(token) > remaining else token
            if not token:
                continue
            elif token in ('|', '&&', ';'):
                color = Gui.SYN_PIPE_COLOR
            elif token in ('>', '>>', '<', '2>&1'):
                color = Gui.SYN_REDIRECT_COLOR
            elif token.startswith('<') and token.endswith('>'):
                color = Gui.SYN_ARG_COLOR
            elif token.startswith('-'):
                color = Gui.SYN_FLAG_COLOR
            elif token.startswith('$'):
                color = Gui.SYN_VAR_COLOR
            else:
                color = Gui.INFO_CMD_COLOR
            try:
                win.addstr(y, pos, display_token, curses.color_pair(color))
                pos += len(display_token)
            except curses.error:
                break
        if len(cmd_str) > max_width - 3:
            try:
                win.addstr(y, x + max_width - 6, "...", curses.color_pair(Gui.BASIC_COLOR))
            except curses.error:
                pass

    @staticmethod
    def prefix_cmdline_with_prefix():
        if config.PREFIX_GLOBALVAR_NAME in Gui.arsenalGlobalVars:
            Gui.cmd.cmdline = f"{Gui.arsenalGlobalVars[config.PREFIX_GLOBALVAR_NAME]} {Gui.cmd.cmdline}"

    def run_continuous(self, stdscr, tmux_handler, has_prefix):
        """
        Continuous mode for tmux - keeps GUI alive across multiple commands
        :param stdscr: curses screen
        :param tmux_handler: callback function to handle tmux command sending
        :param has_prefix: whether to apply prefix to commands
        """
        # Debug logging
        debug_log = open("/tmp/arsenal_gui_debug.log", "a")
        def debug(msg):
            debug_log.write(f"{msg}\n")
            debug_log.flush()

        debug("run_continuous started")
        Gui.init_colors()

        iteration = 0
        while True:
            iteration += 1
            debug(f"Iteration {iteration}: Starting menu")

            # Run the cheats menu to get a command
            self.cheats_menu.run(stdscr)

            debug(f"Iteration {iteration}: Menu returned, Gui.cmd = {Gui.cmd}")

            if Gui.cmd is None:
                # User pressed ESC/F10 to exit
                debug("Gui.cmd is None, exiting")
                break

            debug(f"Iteration {iteration}: Command = {Gui.cmd.cmdline}")

            # Handle internal commands
            if Gui.cmd.cmdline[0] == '>':
                debug("Internal command detected")
                if Gui.cmd.cmdline == ">exit":
                    debug("Exit command, breaking")
                    break
                # Other internal commands handled here if needed
                # For now, just continue
                debug("Continuing after internal command")
                continue

            # Apply prefix if needed
            if has_prefix:
                debug("Applying prefix")
                self.prefix_cmdline_with_prefix()

            debug(f"Calling tmux_handler with: {Gui.cmd.cmdline}")
            if not tmux_handler(Gui.cmd, stdscr):
                debug("tmux_handler returned False, exiting")
                break

            debug(f"Iteration {iteration}: Command sent, looping back")

        debug("run_continuous exiting")
        debug_log.close()

    def run(self, cheatsheets, has_prefix):
        """
        Gui entry point
        :param cheatsheets: cheatsheets dictionary
        """
        if self.cheats_menu is None:
            # Load cheatList if not already done
            self.cheats_menu = CheatslistMenu()
            for value in cheatsheets.values():
                self.cheats_menu.globalcheats.append(value)

        # if global var save exists load it
        if exists(Gui.savefile):
            with open(Gui.savefile, 'r') as f:
                Gui.arsenalGlobalVars = json.load(f)

        wrapper(self.cheats_menu.run)
        if Gui.cmd != None and Gui.cmd.cmdline[0] != '>' and has_prefix:
            self.prefix_cmdline_with_prefix()
        return Gui.cmd
