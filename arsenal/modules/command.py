#Maintainer: @kasem_shibli <https://x.com/kasem_shibli>

import re
import curses
import textwrap

# Import tool detection for impacket command transformation
try:
    from . import tools
    IMPACKET_TOOLS_AVAILABLE = True
except ImportError:
    IMPACKET_TOOLS_AVAILABLE = False
import curses
import textwrap


class Command:
    cmdline = ""
    description = ""
    args = []  # [(name, value)]
    nb_args = 0
    nb_lines_cmd = 1
    nb_lines_desc = 0

    def __init__(self, cheat, gvars):
        self.cmdline = cheat.command

        self.cmd_tags = cheat.command_tags
        self.description = ''
        for tag in self.cmd_tags:
            self.description += '[' + self.cmd_tags[tag] + '] '
        if self.description != '' and cheat.description != '':
            self.description += '\n-----\n'
        self.description += cheat.description

        self.get_args(cheat, gvars)
        self.nb_args = len(self.args)
        # careful this is not the lines number in GUI
        self.nb_lines_cmd = len(cheat.command.split('\n'))
        # careful this is not the lines number in GUI
        self.nb_lines_desc = 0 if cheat.description == '' else len(cheat.description.split('\n'))

    def get_description_cut_by_size(self, size):
        """
        The description cut by lines inside the gui size
        """
        desc_lines = self.description.split('\n')
        result = []
        for line in desc_lines:
            result.extend(textwrap.wrap(line, size))
        return result

    def get_args(self, cheat, gvars):
        """
        Process cmdline from the cheatsheet to get args names
        """
        self.args = []
        # Use a list of tuples here instead of dict in case
        # the cmd has multiple args with the same name..
        for arg_name in re.findall(r'<([^ <>]+)>', cheat.command):
            if "|" in arg_name:  # Format <name|default_value>
                name, var = arg_name.split("|")[:2]
                self.args.append([name, var])
                # Variable has been added to cheat variables before, remove it
                cheat.command = cheat.command.replace(arg_name, name)
                self.cmdline = cheat.command
            elif arg_name in gvars:
                self.args.append([arg_name, gvars[arg_name]])
            elif arg_name in cheat.variables:
                self.args.append([arg_name, cheat.variables[arg_name]])
            else:
                self.args.append([arg_name, ""])

    def get_command_parts(self):
        if self.nb_args != 0:
            regex = ''.join('<' + arg[0] + '>|' for arg in self.args)[:-1]
            cmdparts = re.split(regex, self.cmdline)
        else:
            cmdparts = [self.cmdline]
        return cmdparts

    def build(self):
        """
        Called after argument completion
        -> if some args values are still empty do nothing
        -> else build the final command string by adding args values
        """
        if self.nb_args == 0 :
            return True
        argsval = [a[1] for a in self.args]
        if "" not in argsval:
            # split cmdline at each arg position
            regex = ''.join('<' + arg[0] + '>|' for arg in self.args)[:-1]
            cmdparts = re.split(regex, self.cmdline)
            # concat command parts and arguments values to build the command
            self.cmdline = ""
            for i in range(len(cmdparts) + len(self.args)):
                if i % 2 == 0:
                    self.cmdline += cmdparts[i // 2]
                else:
                    self.cmdline += argsval[(i - 1) // 2]
            
            if IMPACKET_TOOLS_AVAILABLE:
                self.cmdline = self._transform_impacket_commands(self.cmdline)
            # Note: Removed curses.endwin() to allow GUI to restart in tmux mode
            # The wrapper() function handles cleanup when Arsenal actually exits

        # build ok ?
        return "" not in argsval

    def _transform_impacket_commands(self, cmdline):
      
        impacket_format = tools.detect_impacket_format()
        
        if impacket_format is None:
            # No impacket tools detected, leave command unchanged
            return cmdline
        
        # List of impacket tools to transform
        impacket_tools = [
            'psexec', 'smbexec', 'wmiexec', 'atexec',
            'secretsdump', 'samrdump',
            'GetNPUsers', 'GetUserSPNs', 'GetADUsers',
            'getTGT', 'getST', 'ticketer', 'ticketConverter', 'describeTicket',
            'ntlmrelayx', 'smbserver', 'smbclient', 'mssqlclient',
            'rpcdump', 'lookupsid', 'reg', 'services',
            'rbcd', 'goldenPac', 'netview', 'getArch', 'changepasswd',
            'Get-GPPPassword', 'GetLAPSPassword'
        ]
        
        if impacket_format == 'py':
            # Transform: impacket-TOOL → TOOL.py
            for tool in impacket_tools:
                # Match impacket-tool as a whole word (with word boundaries)
                pattern = r'\bimpacket-' + re.escape(tool) + r'\b'
                replacement = tool + '.py'
                cmdline = re.sub(pattern, replacement, cmdline)
        
        elif impacket_format == 'impacket':
            # Transform: TOOL.py → impacket-TOOL
            for tool in impacket_tools:
                # Match tool.py as a whole word
                pattern = r'\b' + re.escape(tool) + r'\.py\b'
                replacement = 'impacket-' + tool
                cmdline = re.sub(pattern, replacement, cmdline)
        
        return cmdline
