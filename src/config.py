"""Configurable properties considered by my program"""

import os
import consts

PROC_PRECISION = 5  # percent values will consts of this many characters


def rows_to_process(nrows):
    # Which rows of the consts.FULLJOIN_PATH file should be considered by generator
    return range(nrows)
    # return range(14)


GEN_PATH = os.path.join(consts.PROJECT_ROOT, 'output')

LOGGING = True
