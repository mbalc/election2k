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

GET_PATH_LIST = GET_GETTER(consts.path_indices, lambda i: i)
GET_ARGS_LIST = GET_GETTER(consts.args_indices, lambda i: int(i))

PATH_LIST = GET_PATH_LIST(0)

def emprt_args_aggr():
    return numpy.zeros(len(consts.args_indices), dtype='int')


ARGS_AGGR = []
for les in range(consts.depth):
    ARGS_AGGR.append(emprt_args_aggr())
LINK_AGGR = [set(), set(), set(), set(), set(), set()]


def create_directory(path):
    """Creates folders that lead to path specified by argument and return path string"""
    aggr = ''

    for elem, formatter in zip([consts.gen_path] + path[1:], consts.format_folder_names[1:]):
        aggr += formatter(elem) + '/'

        if not os.path.isdir(aggr):
            os.mkdir(aggr)

    return aggr


def process_single(new_path, row):
    """Processes single row of the xls file and generates necessary html files"""
    global PATH_LIST, ARGS_AGGR, LINK_AGGR

    args_list = GET_ARGS_LIST(row)

    for i in reversed(range(consts.depth)):
        if PATH_LIST[i] == new_path[i]:
            break

        subdirlist = PATH_LIST[:i + 1]
        subpath = create_directory(subdirlist)

        output = template_engine.create_webpage(ARGS_AGGR[i], LINK_AGGR[i], [subdirlist, subpath])
        # print('out: ', output)
        file = open(subpath + "index.html", 'wb')
        file.write(output.encode(consts.UTF))

        ARGS_AGGR[i] = emprt_args_aggr()
        LINK_AGGR[i] = set()

    nparr = numpy.asarray(args_list)
    # print(nparr, ARGS_AGGR[0], ARGS_AGGR[0]+nparr)

    for i in range(consts.depth):
        # print(i, '-', ARGS_AGGR[i] + numpy.asarray(args_list))
        ARGS_AGGR[i] += nparr
    for i in range(consts.depth - 1):
        LINK_AGGR[i].add(consts.format_folder_names[i](new_path[i + 1]))

    PATH_LIST = new_path


# write_template(create_directory(path_list), [])

NROWS = config.how_many_rows(main.nrows)

for row_num in range(NROWS):
    # print(row_num, ": ", ARGS_AGGR)
    process_single(GET_PATH_LIST(row_num), row_num)
process_single(['dynks'] * consts.depth, NROWS - 1)
