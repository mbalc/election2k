import consts
import xlrd

zal1 = xlrd.open_workbook('../data/zal1.xls', 'r').sheet_by_name('Zal1')

def fetch_okregi():
    first_row, last_row = (consts.zal1[k] for k in ('first_row', 'last_row'))
    nr_okr, siedziba = (consts.zal1['columns'][k] for k in ('nr_okr', 'siedziba'))

    print(first_row)
    print(nr_okr)
    print(siedziba)

    output = {}

    get_nr_okr = lambda row: zal1.cell_value(row, nr_okr)
    get_siedziba = lambda row: zal1.cell_value(row, siedziba)

    wojewodztwo_prefix = get_nr_okr(first_row)
    last_wojewodztwo = ''

    def nameof_wojewodztwo(): return 'Woj. ' + last_wojewodztwo.lower()
    nameof_okreg = lambda row: get_siedziba(row) + '(okręg nr ' + str(int(get_nr_okr(row))) + ')'

    for i in range(first_row, last_row):
        print(nameof_wojewodztwo())
        print(wojewodztwo_prefix + ' ' + last_wojewodztwo)
        if get_nr_okr(i) == wojewodztwo_prefix:
            last_wojewodztwo = get_siedziba(i)
            output[nameof_wojewodztwo()] = {}
        else:
            output[nameof_wojewodztwo()][nameof_okreg(i)] = {}


    return output

print(fetch_okregi())
