#Maintainer: @kasem_shibli <https://x.com/kasem_shibli>

import os
from os.path import dirname, abspath, expanduser, join

# Base paths
DATAPATH = join(dirname(dirname(abspath(__file__))), 'data')
BASEPATH = dirname(dirname(dirname(abspath(__file__))))
HOMEPATH = expanduser("~")
FORMATS = ["md", "rst", "yml", "cheat"]
EXCLUDE_LIST = ["README.md", "README.rst", "index.rst"]
FUZZING_DIRS = ["/usr/local/share/wordlists/**/*.txt"]

CHEATS_PATHS = [
    join(DATAPATH, "cheats"),
    join(BASEPATH, "my_cheats"),
    join(HOMEPATH, ".cheats"),
    "/opt/my-resources/my-cheats",
    "/opt/my-resources/setup/arsenal-cheats"
]

NAVI_CHEATS_PATHS = [
    join(HOMEPATH, ".local/share/navi/cheats"),
    join(HOMEPATH, ".config/navi/cheats"),
    "/usr/share/navi/cheats"
]

messages_error_missing_arguments = 'Error missing arguments'

# set lower delay to use ESC key (in ms)
os.environ.setdefault('ESCDELAY', '25')
os.environ['TERM'] = 'xterm-256color'

if os.environ.get('ARSENAL_LOCAL'):
    savevarfile = join(os.getcwd(), ".arsenal.json")
    historyfile = join(os.getcwd(), ".arsenal_history.json")
    favoritesfile = join(os.getcwd(), ".arsenal_favorites.json")
else:
    savevarfile = join(HOMEPATH, ".arsenal.json")
    historyfile = join(HOMEPATH, ".arsenal_history.json")
    favoritesfile = join(HOMEPATH, ".arsenal_favorites.json")

PREFIX_GLOBALVAR_NAME = "arsenal_prefix_cmd"
MAX_HISTORY_SIZE = 50
