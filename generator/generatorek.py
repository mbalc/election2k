import os
import xlrd
import numpy

import consts
import config
import template_engine

main = xlrd.open_workbook('../data/fullOuterJoin.xls', 'r').sheet_by_index(0)

GET_GETTER = (lambda indices, rett: (
    lambda row: (
        list(map(
            lambda i: (
                rett(main.cell_value(row, i))
            )
            , indices
        ))
    )
))

GET_PATH_LIST = GET_GETTER(consts.PATH_INDICES, lambda i: i)
GET_ARGS_LIST = GET_GETTER(consts.ARGS_INDICES, lambda i: int(i))

PATH_LIST = GET_PATH_LIST(0)

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


def create_directory(path):
    """Creates folders that lead to path specified by argument and return path string"""
    aggr = ''

    for elem, formatter in zip([consts.GEN_PATH] + path[1:], consts.FORMAT_FOLDER_NAMES[1:]):
        aggr += formatter(elem) + '/'

        if not os.path.isdir(aggr):
            os.mkdir(aggr)

    return aggr


def process_single(new_path, row):
    """Processes single row of the xls file and generates necessary html files"""
    global PATH_LIST, ARGS_AGGR, LINK_AGGR

    args_list = GET_ARGS_LIST(row)

    for i in reversed(range(consts.DEPTH)):
        if PATH_LIST[i] == new_path[i]:
            break

        subdirlist = PATH_LIST[:i + 1]
        subpath = create_directory(subdirlist)

        # output = template_engine.create_webpage(ARGS_AGGR[i], LINK_AGGR[i], [subdirlist, subpath])
        output = template_engine.create_webpage(ARGS_AGGR[i], LINK_AGGR[i], [subdirlist])
        file = open(subpath + "index.html", 'wb')
        file.write(output.encode(consts.UTF))

        ARGS_AGGR[i] = get_empty_args()
        LINK_AGGR[i] = set()

    nparr = numpy.asarray(args_list)

    for i in range(consts.DEPTH):
        ARGS_AGGR[i] += nparr
    for i in range(consts.DEPTH - 1):
        LINK_AGGR[i].add(consts.FORMAT_FOLDER_NAMES[i](new_path[i + 1]))

    PATH_LIST = new_path


# write_template(create_directory(path_list), [])

NROWS = config.how_many_rows(main.nrows)

for row_num in range(NROWS):
    process_single(GET_PATH_LIST(row_num), row_num)
process_single(['dynks'] * consts.DEPTH, NROWS - 1)
