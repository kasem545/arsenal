import argparse
import json
import os
import fcntl
import termios
import re
import time
from curses import wrapper

# arsenal
from . import __version__
from .modules import config
from .modules import cheat
from .modules import check
from .modules import gui as arsenal_gui


class App:

    def __init__(self):
        pass

    def get_args(self):
        examples = '''examples:
        arsenal
        arsenal --copy
        arsenal --print

        You can manage global variables with:
        >set GLOBALVAR1=<value>
        >show
        >clear

        (cmd starting with '>' are internals cmd)
        '''

        parser = argparse.ArgumentParser(
            prog="arsenal",
            description='arsenal v{} - Pentest command launcher'.format(__version__),
            epilog=examples,
            formatter_class=argparse.RawTextHelpFormatter
        )

        group_out = parser.add_argument_group('output [default = prefill]')
        group_out.add_argument('-p', '--print', action='store_true', help='Print the result')
        group_out.add_argument('-o', '--outfile', action='store', help='Output to file')
        group_out.add_argument('-x', '--copy', action='store_true', help='Output to clipboard')
        group_out.add_argument('-e', '--exec', action='store_true', help='Execute cmd')
        group_out.add_argument('-t', '--tmux', action='store_true', help='Send command to tmux panel')
        group_out.add_argument('-c', '--check', action='store_true', help='Check the existing commands')
        group_out.add_argument('-f', '--prefix', action='store_true', help='command prefix')
        group_out.add_argument('--no-tags', action='store_false', help='Whether or not to show the'
                                                                       ' tags when drawing the cheats')
        parser.add_argument('-V', '--version', action='version', version='%(prog)s (version {})'.format(__version__))

        return parser.parse_args()

    def run(self):
        args = self.get_args()

        # load cheatsheets
        cheatsheets = cheat.Cheats().read_files(config.CHEATS_PATHS, config.FORMATS,
                                                config.EXCLUDE_LIST)

        if args.check:
            check.check(cheatsheets)
        else:
            self.start(args, cheatsheets)

    def start(self, args, cheatsheets):
        arsenal_gui.Gui.with_tags = args.no_tags

        # create gui object
        gui = arsenal_gui.Gui()

        # Load cheat list
        for value in cheatsheets.values():
            if gui.cheats_menu is None:
                gui.cheats_menu = arsenal_gui.CheatslistMenu()
            gui.cheats_menu.globalcheats.append(value)

        # Load global vars if they exist
        if os.path.exists(config.savevarfile):
            with open(config.savevarfile, 'r') as f:
                arsenal_gui.Gui.arsenalGlobalVars = json.load(f)

        # For tmux mode, use continuous GUI mode
        if args.tmux:
            try:
                import libtmux

                # Debug log file
                debug_log = open("/tmp/arsenal_debug.log", "w")

                def debug(msg):
                    debug_log.write(f"{msg}\n")
                    debug_log.flush()

                def tmux_handler(cmd):
                    """Handler function to send commands to tmux pane"""
                    try:
                        debug(f"Sending command to tmux: {cmd.cmdline}")
                        server = libtmux.Server()
                        session = server.sessions[-1]  # Updated API for libtmux >= 0.17

                        # Get the current window where arsenal is running
                        current_pane_id = os.environ.get('TMUX_PANE')
                        window = None
                        if current_pane_id:
                            debug(f"Looking for current pane: {current_pane_id}")
                            for win in session.windows:
                                for p in win.panes:
                                    if p.pane_id == current_pane_id:
                                        window = win
                                        debug(f"Found current window: {window.window_id}")
                                        break
                                if window:
                                    break

                        # Fallback to active window if current window not found
                        if not window:
                            debug("Current window not found, using active window")
                            window = session.active_window

                        panes = window.panes
                        debug(f"Found {len(panes)} panes")

                        if len(panes) == 1:
                            # split window to get more pane
                            debug("Splitting window...")
                            pane = window.split(attach=False)  # Updated API for libtmux >= 0.33
                            time.sleep(0.3)
                        else:
                            pane = panes[-1]
                            debug(f"Using existing pane: {pane.pane_id}")

                        # send command to other pane (Arsenal stays focused)
                        if args.exec:
                            debug("Executing command with Enter")
                            pane.send_keys(cmd.cmdline)
                        else:
                            debug("Prefilling command without Enter")
                            pane.send_keys(cmd.cmdline, enter=False)

                        debug("Command sent successfully")
                        return True  # Success
                    except libtmux.exc.LibTmuxException as e:
                        debug(f"Arsenal tmux error: {e}")
                        return False  # Failure
                    except Exception as e:
                        debug(f"Arsenal unexpected error: {e}")
                        import traceback
                        debug(traceback.format_exc())
                        return False  # Failure

                # Run GUI in continuous mode with wrapper
                debug("Starting Arsenal in continuous tmux mode...")
                wrapper(lambda stdscr: gui.run_continuous(stdscr, tmux_handler, args.prefix))
                debug("Arsenal tmux mode exited")
                debug_log.close()
                return

            except ImportError:
                print("Arsenal: libtmux not installed. Falling back to standard mode.")
                # Fall through to standard mode

        # Standard (non-tmux) mode
        while True:
            # launch gui
            cmd = gui.run(cheatsheets, args.prefix)

            if cmd == None:
                exit(0)

            # Internal CMD
            elif cmd.cmdline[0] == '>':
                if cmd.cmdline == ">exit":
                    break
                elif cmd.cmdline == ">show":
                    if (os.path.exists(config.savevarfile)):
                        with open(config.savevarfile, 'r') as f:
                            arsenalGlobalVars = json.load(f)
                            for k, v in arsenalGlobalVars.items():
                                print(k + "=" + v)
                    break
                elif cmd.cmdline == ">clear":
                    with open(config.savevarfile, "w") as f:
                        f.write(json.dumps({}))
                    self.run()
                elif re.match(r"^\>set( [^= ]+=[^= ]+)+$", cmd.cmdline):
                    # Load previous global var
                    if (os.path.exists(config.savevarfile)):
                        with open(config.savevarfile, 'r') as f:
                            arsenalGlobalVars = json.load(f)
                    else:
                        arsenalGlobalVars = {}
                    # Add new glovar var
                    varlist = re.findall("([^= ]+)=([^= ]+)", cmd.cmdline)
                    for v in varlist:
                        arsenalGlobalVars[v[0]] = v[1]
                    with open(config.savevarfile, "w") as f:
                        f.write(json.dumps(arsenalGlobalVars))
                else:
                    print("Arsenal: invalid internal command..")
                    break

            # OPT: Copy CMD to clipboard
            elif args.copy:
                try:
                    import pyperclip
                    pyperclip.copy(cmd.cmdline)
                except ImportError:
                    pass
                break

            # OPT: Only print CMD
            elif args.print:
                print(cmd.cmdline)
                break

            # OPT: Write in file
            elif args.outfile:
                with open(args.outfile, 'w') as f:
                    f.write(cmd.cmdline)
                break

            # OPT: Exec
            elif args.exec:
                os.system(cmd.cmdline)
                break

            # DEFAULT: Prefill Shell CMD
            else:
                self.prefil_shell_cmd(cmd)
                break

    def prefil_shell_cmd(self, cmd):
        stdin = 0
        # save TTY attribute for stdin
        oldattr = termios.tcgetattr(stdin)
        # create new attributes to fake input
        newattr = termios.tcgetattr(stdin)
        # disable echo in stdin -> only inject cmd in stdin queue (with TIOCSTI)
        newattr[3] &= ~termios.ECHO
        # enable non canonical mode -> ignore special editing characters
        newattr[3] &= ~termios.ICANON
        # use the new attributes
        termios.tcsetattr(stdin, termios.TCSANOW, newattr)
        # write the selected command in stdin queue
        try:
            for c in cmd.cmdline:
                fcntl.ioctl(stdin, termios.TIOCSTI, c)
        except OSError:
            message = "========== OSError ============\n"
            message += "Arsenal needs TIOCSTI enable for running\n"
            message += "Please run the following commands as root to fix this issue on the current session :\n"
            message += "sysctl -w dev.tty.legacy_tiocsti=1\n"
            message += "If you want this workaround to survive a reboot,\n" 
            message += "add the following configuration to sysctl.conf file and reboot :\n"
            message += "echo \"dev.tty.legacy_tiocsti=1\" >> /etc/sysctl.conf\n"
            message += "More details about this bug here: https://github.com/Orange-Cyberdefense/arsenal/issues/77"
            print(message)
        # restore TTY attribute for stdin
        termios.tcsetattr(stdin, termios.TCSADRAIN, oldattr)


def main():
    try:
        App().run()
    except KeyboardInterrupt:
        exit(0)


if __name__ == "__main__":
    wrapper(main()) 
