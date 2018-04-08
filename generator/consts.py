ZAL1 = {
    'first_row': 6,
    'last_row': 90,
    'columns': {
        'nr_okr': 0,
        'siedziba': 1,
        'last_col': 10,
    },
}

PROJECT_ROOT = '..'

OBW_PATH = PROJECT_ROOT + '/data/obwody/'
EXAMPLE = 'obw01.xls'

GEN_PATH = PROJECT_ROOT + '/output'

TEMPLATE_DIR = PROJECT_ROOT + '/templates'
TEMPLATE_PATH = TEMPLATE_DIR + '/main.html'

STYLESHEET_NAME = 'stylesheet.css'
STYLESHEET_PATH = TEMPLATE_DIR + STYLESHEET_NAME

PATH_INDICES = [2, 0, 1, 5, 7]
ARGS_INDICES = list(range(10, 27))

DEPTH = len(PATH_INDICES)

ISO = 'iso-8859-1'
UTF = 'utf-8'

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
    lambda i: str(int(float(i))),
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
