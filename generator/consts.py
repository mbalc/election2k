zal1 = {
    'first_row': 6,
    'last_row': 90,
    'columns': {
        'nr_okr': 0,
        'siedziba': 1,
        'last_col': 10,
    },
}

project_root = '..'

obw_path = project_root + '/data/obwody/'
example = 'obw01.xls'

gen_path = project_root + '/output'

template_dir = project_root + '/templates'
template_path = template_dir + '/main.html'

stylesheet_name = 'stylesheet.css'
stylesheet_path = template_dir + stylesheet_name

path_indices = [2,0,1,5,7]
args_indices = list(range(10, 27))

depth = len(path_indices)

ISO = 'iso-8859-1'
UTF = 'utf-8'

kandydaci = [
    "GRABOWSKI Dariusz",
    "IKONOWICZ Piotr",
    "KALINOWSKI Jarosław",
    "KORWIN-MIKKE Janus",
    "KRZAKLEWSKI Maria",
    "KWAŚNIEWSKI Aleksander",
    "LEPPER Andrzej",
    "ŁOPUSZAŃSKI Jan",
    "OLECHOWSKI Andrzej",
    "PAWŁOWSKI Bogdan",
    "WAŁĘSA Lech",
    "WILECKI Tadeusz",
]

format_folder_names = [
    lambda i: i,
    lambda i: i,
    lambda i: i,
    lambda i: i,
    lambda i: i,
    lambda i: str(int(float(i))),
]

format_button_names = [
    lambda i: i,
    lambda i: i,
    lambda i: i,
    lambda i: i,
    lambda i: i,
    lambda i: 'Okręg ' + str(int(float(i))),
]

nameof_wojewodztwo = lambda name: 'Woj. ' + name.lower()
nameof_okreg = lambda siedziba, nr_okr: siedziba + '(okręg nr ' + str(int(nr_okr)) + ')'
