"""Library with properties used by this package that are constant either because of the way XLS
election files are written or because of my file organization decisions"""

import os

SRC_PATH = os.path.dirname(__file__)

PROJECT_ROOT = os.path.join(SRC_PATH, '..')

OBW_PATH = os.path.join(PROJECT_ROOT, 'data/obwody/')
EXAMPLE = 'obw01.xls'

TEMPLATE_DIR = os.path.join(PROJECT_ROOT, 'templates/')
TEMPLATE_PATH = os.path.join(TEMPLATE_DIR, 'main.html')

STYLESHEET_NAME = 'stylesheet.css'
STYLESHEET_PATH = os.path.join(TEMPLATE_DIR, STYLESHEET_NAME)

FULLJOIN_PATH = os.path.join(PROJECT_ROOT, 'data/fullOuterJoin.xls')

PATH_INDICES = [2, 0, 1, 5, 7]
ARGS_INDICES = list(range(10, 27))

DEPTH = len(PATH_INDICES)

ISO = 'iso-8859-1'
UTF = 'utf-8'

ZAL1 = {
    'path': os.path.join(PROJECT_ROOT, 'data/zal1.xls'),
    'first_row': 6,
    'last_row': 90,
    'columns': {
        'nr_okr': 0,
        'siedziba': 1,
        'last_col': 10,
    },
}

KANDYDACI = [
    "GRABOWSKI Dariusz",
    "IKONOWICZ Piotr",
    "KALINOWSKI Jarosław",
    "KORWIN-MIKKE Janusz",
    "KRZAKLEWSKI Maria",
    "KWAŚNIEWSKI Aleksander",
    "LEPPER Andrzej",
    "ŁOPUSZAŃSKI Jan",
    "OLECHOWSKI Andrzej",
    "PAWŁOWSKI Bogdan",
    "WAŁĘSA Lech",
    "WILECKI Tadeusz",
]

FORMAT_FOLDER_NAMES = [
    lambda i: i,
    lambda i: i,
    lambda i: i,
    lambda i: i,
    lambda i: i,
    lambda i: 'okr' + str(int(float(i))),
]

FORMAT_BUTTON_NAMES = [
    lambda i: i,
    lambda _: 'Polska',
    lambda i: i,
    lambda i: i,
    lambda i: i,
    lambda i: 'Okręg ' + str(int(float(i))),
]

NAMEOF_WOJEWODZTWO = lambda name: 'Woj. ' + name.lower()
NAMEOF_OKREG = lambda siedziba, nr_okr: siedziba + '(okręg nr ' + str(int(nr_okr)) + ')'

OBW_FILES = [OBW_PATH + 'obw%02d.xls' % obw_id for obw_id in range(1, 69)]
