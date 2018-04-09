import config
import shutil

import sys

NEED_NEWLINE = False

def log(*args, **kwargs):
    if config.LOGGING:
        global NEED_NEWLINE
        if NEED_NEWLINE:
            print()  # newline
            NEED_NEWLINE = False
        print(*args, **kwargs)

def live(str):
    if config.LOGGING:
        global NEED_NEWLINE
        NEED_NEWLINE = True
        length = shutil.get_terminal_size((80, 20)).columns
        if (len(str) > length):
            str = str[:length-2] + '...'
        sys.stdout.write(str + (' ' * (length - len(str))) + '\r')
        sys.stdout.flush()
