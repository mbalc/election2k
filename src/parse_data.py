"""Parses data fetched with /initData.sh to a single file with all info necessary for generator
to process"""

import re

import xlrd
import xlwt

import consts

from logger import log, live

ZAL1 = xlrd.open_workbook(consts.ZAL1['path'], 'r').sheet_by_name('Zal1')

FIRST_ROW, LAST_ROW = (consts.ZAL1[k] for k in ('first_row', 'last_row'))
NR_OKR, SIEDZIBA = (consts.ZAL1['columns'][k] for k in ('nr_okr', 'siedziba'))


def get_siedziba(row):
    """ - """
    return ZAL1.cell_value(row, SIEDZIBA)


def get_nr_okr(row):
    """ - """
    return ZAL1.cell_value(row, NR_OKR)


def nameof_wojewodztwo(last):
    """ - """
    return consts.NAMEOF_WOJEWODZTWO(last)


def nameof_okreg(row):
    """ - """
    return consts.NAMEOF_OKREG(get_siedziba(row), get_nr_okr(row))


def fetch_mappings():
    """Maps identifiers of entities to their full names"""
    output = {'województwa': {}, 'okręgi': {}}

    wojewodztwo_prefix = get_nr_okr(FIRST_ROW)

    woj = 2

    for idx in range(FIRST_ROW, LAST_ROW):
        new_nr = get_nr_okr(idx)
        if new_nr == wojewodztwo_prefix:
            last_wojewodztwo = get_siedziba(idx)
            output['województwa']['%02d' % woj] = nameof_wojewodztwo(last_wojewodztwo)
            woj += 2
        else:
            output['okręgi'][new_nr] = nameof_okreg(idx)

    return output


def make_join():
    """Concatenates 'obw' files into one, appends additional info and writes to a new file"""
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet('join')

    mappings = fetch_mappings()

    row = -1

    get_woj_code = re.compile(r'^[0-9]{2}')

    for obw_file in consts.OBW_FILES:
        live('Parsing file ' + obw_file + '...')
        source = xlrd.open_workbook(obw_file, 'r').sheet_by_index(0)
        for i in range(1, source.nrows):
            row += 1
            for j in range(source.ncols):
                sheet.write(row, j + 3, source.cell(i, j).value)

            kod_okregu = source.cell_value(i, 0)
            kod_gminy = source.cell_value(i, 1)
            sheet.write(row, 0, mappings['województwa'][get_woj_code.search(kod_gminy)[0]])
            sheet.write(row, 1, mappings['okręgi'][kod_okregu])
            sheet.write(row, 2, '')

    log('\nWriting result to ', consts.FULLJOIN_PATH, '...')
    workbook.save(consts.FULLJOIN_PATH)

    log('Done!')

make_join()
