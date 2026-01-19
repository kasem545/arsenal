import argparse
import json
import os
import fcntl
import termios
import re
import sys
import time
from curses import wrapper

# arsenal
from . import __version__
from .modules import config
from .modules import cheat
from .modules import check
from .modules import repo
from .modules import gui as arsenal_gui


class App:

    def __init__(self):
        pass

    def get_args(self):
        examples = '''examples:
        arsenal
        arsenal --copy
        arsenal --print

        Repo management:
        arsenal repo add denisidoro/cheats
        arsenal repo list
        arsenal repo remove denisidoro/cheats
        arsenal repo update
        arsenal repo browse

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

        subparsers = parser.add_subparsers(dest='command', help='sub-commands')

        repo_parser = subparsers.add_parser('repo', help='Manage cheatsheet repositories')
        repo_subparsers = repo_parser.add_subparsers(dest='repo_command', help='repo commands')

        repo_add = repo_subparsers.add_parser('add', help='Add a cheatsheet repo')
        repo_add.add_argument('repo_name', help='Repository (e.g., denisidoro/cheats)')

        repo_remove = repo_subparsers.add_parser('remove', help='Remove a cheatsheet repo')
        repo_remove.add_argument('repo_name', help='Repository to remove')

        repo_subparsers.add_parser('list', help='List installed repos')
        repo_subparsers.add_parser('update', help='Update all repos')
        repo_subparsers.add_parser('browse', help='Browse popular repos')

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

        if args.command == 'repo':
            self.handle_repo_command(args)
            return

        cheats_obj = cheat.Cheats()
        all_paths = config.CHEATS_PATHS + getattr(config, 'NAVI_CHEATS_PATHS', []) + repo.get_all_repo_paths()
        cheatsheets = cheats_obj.read_files(all_paths, config.FORMATS, config.EXCLUDE_LIST)

        if args.check:
            check.check(cheatsheets)
        else:
            self.start(args, cheatsheets)

    def handle_repo_command(self, args):
        if args.repo_command == 'add':
            repo.add_repo(args.repo_name)
        elif args.repo_command == 'remove':
            repo.remove_repo(args.repo_name)
        elif args.repo_command == 'list':
            repo.show_repos()
        elif args.repo_command == 'update':
            repo.update_repo()
        elif args.repo_command == 'browse':
            repo.browse_repos()
        else:
            print("Usage: arsenal repo <add|remove|list|update|browse>")
            print("Run 'arsenal repo --help' for more info")

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

        if args.tmux:
            if not os.environ.get('TMUX'):
                print("Arsenal: Starting tmux session...")
                arsenal_cmd = "arsenal " + " ".join(sys.argv[1:])
                os.execvp("tmux", ["tmux", "new-session", "-s", "arsenal", arsenal_cmd])
                return

            try:
                import libtmux

                # Debug log file
                debug_log = open("/tmp/arsenal_debug.log", "w")

                def debug(msg):
                    debug_log.write(f"{msg}\n")
                    debug_log.flush()

                def get_all_panes_info(server, current_pane_id):
                    """Get info about all available tmux panes"""
                    panes_info = []
                    for session in server.sessions:
                        for window in session.windows:
                            for pane in window.panes:
                                panes_info.append({
                                    'pane_id': pane.pane_id,
                                    'pane': pane,
                                    'window': window,
                                    'session_name': session.session_name,
                                    'window_name': window.window_name,
                                    'window_index': window.window_index,
                                    'pane_index': pane.pane_index,
                                    'current_path': pane.pane_current_path,
                                    'is_current': pane.pane_id == current_pane_id
                                })
                    return panes_info

                def tmux_handler(cmd, stdscr):
                    """Handler function to send commands to tmux pane"""
                    try:
                        debug(f"Sending command to tmux: {cmd.cmdline}")
                        server = libtmux.Server()
                        current_pane_id = os.environ.get('TMUX_PANE')
                        
                        panes_info = get_all_panes_info(server, current_pane_id)
                        other_panes = [p for p in panes_info if p['pane_id'] != current_pane_id]
                        debug(f"Found {len(other_panes)} other panes")
                        
                        current_window_index = None
                        for p in panes_info:
                            if p['pane_id'] == current_pane_id:
                                current_window_index = p['window_index']
                                break
                        
                        target_pane = None
                        
                        current_window = None
                        current_session = None
                        for p in panes_info:
                            if p['pane_id'] == current_pane_id:
                                current_window = p['window']
                                for sess in server.sessions:
                                    if sess.session_name == p['session_name']:
                                        current_session = sess
                                        break
                                break
                        
                        if not current_session:
                            current_session = server.sessions[-1]
                        if not current_window:
                            current_window = current_session.active_window
                        
                        if len(other_panes) == 0:
                            debug("No other panes, creating new one...")
                            target_pane = current_window.split(attach=False)
                            time.sleep(0.3)
                        else:
                            debug(f"Showing pane selector with {len(other_panes)} panes...")
                            selector = arsenal_gui.TmuxPaneSelectorMenu(
                                gui.cheats_menu, 
                                panes_info,
                                current_pane_id,
                                current_window_index
                            )
                            result = selector.run(stdscr)
                            
                            if result is None:
                                debug("User cancelled pane selection")
                                return True
                            elif result == 'new_subpane':
                                debug("User requested new sub-pane")
                                target_pane = current_window.split(attach=False)
                                time.sleep(0.3)
                            elif result == 'new_pane':
                                debug("User requested new pane")
                                new_window = current_session.new_window(attach=False)
                                target_pane = new_window.active_pane
                                time.sleep(0.3)
                            else:
                                target_pane = result['pane']
                                debug(f"User selected pane: {target_pane.pane_id}")
                        
                        if args.exec:
                            debug("Executing command with Enter")
                            target_pane.send_keys(cmd.cmdline)
                        else:
                            debug("Prefilling command without Enter")
                            target_pane.send_keys(cmd.cmdline, enter=False)

                        debug("Command sent successfully")
                        return True
                    except libtmux.exc.LibTmuxException as e:
                        debug(f"Arsenal tmux error: {e}")
                        return False
                    except Exception as e:
                        debug(f"Arsenal unexpected error: {e}")
                        import traceback
                        debug(traceback.format_exc())
                        return False

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
