import xlrd
import xlwt

import os
import re

import consts


def fetch_mappings():
    zal1 = xlrd.open_workbook('../data/zal1.xls', 'r').sheet_by_name('Zal1')

    first_row, last_row = (consts.zal1[k] for k in ('first_row', 'last_row'))
    nr_okr, siedziba = (consts.zal1['columns'][k] for k in ('nr_okr', 'siedziba'))

    output = { 'województwa': {}, 'okręgi': {}}

    get_nr_okr = lambda row: zal1.cell_value(row, nr_okr)
    get_siedziba = lambda row: zal1.cell_value(row, siedziba)

    wojewodztwo_prefix = get_nr_okr(first_row)
    last_wojewodztwo = ''

    def nameof_wojewodztwo(): return consts.nameof_wojewodztwo(last_wojewodztwo)
    nameof_okreg = lambda row: consts.nameof_okreg(get_siedziba(row), get_nr_okr(row))

    woj = 2

    for i in range(first_row, last_row):
        if get_nr_okr(i) == wojewodztwo_prefix:
            last_wojewodztwo = get_siedziba(i)
            output['województwa']['%02d' % woj] = nameof_wojewodztwo()
            woj += 2
        else:
            output['okręgi'][get_nr_okr(i)] = nameof_okreg(i)

    return output

def make_join():
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet('join')

    mappings = fetch_mappings()

    row = -1
    # source = xlrd.open_workbook(consts.obw_path + consts.example, 'r').sheet_by_index(0)
    #
    # for j in range(source.ncols):
    #     sheet.write(row, j + 2, re.sub('\n', ' ', source.cell(row, j).value))
    #
    # sheet.write(row, 0, 'Województwo')
    # sheet.write(row, 1, 'Okręg')

    get_woj_code = re.compile(r'^[0-9]{2}')

    for i in range(1, 69):
        source = xlrd.open_workbook(consts.obw_path + 'obw%02d.xls' % i, 'r').sheet_by_index(0)
        for i in range(1, source.nrows):
            row += 1
            for j in range(source.ncols):
                sheet.write(row, j + 2, source.cell(i, j).value)

            kod_okregu = source.cell_value(i, 0)
            kod_gminy = source.cell_value(i, 1)
            sheet.write(row, 0, mappings['województwa'][get_woj_code.search(kod_gminy)[0]])
            sheet.write(row, 1, mappings['okręgi'][kod_okregu])


    workbook.save('../data/fullOuterJoin.xls')

make_join()
