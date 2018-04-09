"""Analyses data row-by-row, aggregating it for each depth and unloading it into a new webpage
for relevant entity of a given depth when all its subentities were already analyzed"""

import os
import shutil
import xlrd
import numpy

import consts
import config
import template_engine

from logger import log, live

main = xlrd.open_workbook(consts.FULLJOIN_PATH, 'r').sheet_by_index(0)


def get_path_list(row):
    return list(map(lambda i: (main.cell_value(row, i)), consts.PATH_INDICES))


def get_args_list(row):
    return list(map(lambda i: (main.cell_value(row, i)), consts.ARGS_INDICES))


def get_empty_set():
    return set()


def get_empty_args():
    return numpy.zeros(len(consts.ARGS_INDICES), dtype='int')


ARGS_AGGR = []
for _ in range(consts.DEPTH):
    ARGS_AGGR.append(get_empty_args())

LINK_AGGR = []
for _ in range(consts.DEPTH):
    LINK_AGGR.append(get_empty_set())

PATH_LIST = get_path_list(0)


def create_directory(path):
    """Creates folders that lead to path specified by argument and return path string"""
    aggr = ''

    for path, formatter in zip([config.GEN_PATH] + path[1:], consts.FORMAT_FOLDER_NAMES[1:]):
        aggr = os.path.join(aggr, formatter(path))

        if not os.path.isdir(aggr):
            os.mkdir(aggr)

    return aggr


def process_single(new_path, row):
    """Processes single row of the xls file and generates necessary html files"""
    global PATH_LIST, ARGS_AGGR, LINK_AGGR

    args_list = get_args_list(row)

    for i in reversed(range(consts.DEPTH)):
        if PATH_LIST[i] == new_path[i]:
            break

        subdirlist = PATH_LIST[:i + 1]
        subpath = create_directory(subdirlist)

        live('\rWriting ' + os.path.relpath(subpath, config.GEN_PATH))

        output = template_engine.create_webpage(ARGS_AGGR[i], LINK_AGGR[i], [subdirlist])
        file = open(os.path.join(subpath, 'index.html'), 'wb')
        file.write(output.encode(consts.UTF))

        ARGS_AGGR[i] = get_empty_args()
        LINK_AGGR[i] = set()

    nparr = numpy.asarray(args_list, dtype='int')

    for i in range(consts.DEPTH):
        ARGS_AGGR[i] += nparr
    for i in range(consts.DEPTH - 1):
        LINK_AGGR[i].add(consts.FORMAT_FOLDER_NAMES[i](new_path[i + 1]))

    PATH_LIST = new_path


ROW_NUMS = config.rows_to_process(main.nrows)

log('Writing in path ', config.GEN_PATH)

for row_num in ROW_NUMS:
    process_single(get_path_list(row_num), row_num)

process_single(['uniqueString'] * consts.DEPTH, row_num)

shutil.copy(consts.STYLESHEET_PATH, config.GEN_PATH)

log('Done!')
