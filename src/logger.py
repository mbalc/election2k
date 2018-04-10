"""Logging-related procedures"""

import sys
import shutil

import config

NEED_NEWLINE = False


def log(*args, **kwargs):
    """Log only if logging is enabled"""
    if config.LOGGING:
        global NEED_NEWLINE
        if NEED_NEWLINE:
            print()  # newline
            NEED_NEWLINE = False
        print(*args, **kwargs)


def live(out):
    """Log over previous line of log, provided that logging is enabled by the user"""
    if config.LOGGING:
        global NEED_NEWLINE
        NEED_NEWLINE = True
        length = shutil.get_terminal_size((80, 20)).columns
        if len(out) > length:
            out = out[:length - 2] + '...'
        sys.stdout.write(out + (' ' * (length - len(out))) + '\r')
        sys.stdout.flush()
