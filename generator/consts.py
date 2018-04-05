zal1 = {
    'first_row': 6,
    'last_row': 90,
    'columns': {
        'nr_okr': 0,
        'siedziba': 1,
        'last_col': 10,
    },
    'headers': [
        'Liczba obwodów głosowania',
        'Liczba uprawnionych do głosowania',
		'Liczba wydanych kart do głosowania',
        'Procent wydanych kart do głosowania (frekwencja)',
        'Liczba oddanych głosów',
        'Liczba głosów ważnych',
        'Procent głosów ważnych',
        'Liczba głosów nieważnych',
        'Procent głosów nieważnych',
     ]
}

project_root = '..'

obw_path = project_root + '/data/obwody/'
example = 'obw01.xls'

gen_path = project_root + '/output'

path_indices = [0,1,4,6]
args_indices = list(range(9, 11))

depth = 5


format_folder_names = [  # TODO
    lambda i: i,
    lambda i: i,
    lambda i: i,
    lambda i: i,
    lambda i: str(int(float(i))),
]

nameof_wojewodztwo = lambda name: 'Woj. ' + name.lower()
nameof_okreg = lambda siedziba, nr_okr: siedziba + '(okręg nr ' + str(int(nr_okr)) + ')'
