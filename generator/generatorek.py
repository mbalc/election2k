# from Tools.scripts.treesync import create_directories
#
# from django.template import Context
# from django.template.engine import Engine
# from django.conf import settings
# from config import configuration

import xlrd, os, numpy

import consts


main = xlrd.open_workbook('../data/fullOuterJoin.xls', 'r').sheet_by_index(0)

get_getter = lambda indices, rett: lambda row: list(map(lambda i: rett(main.cell_value(row, i)), indices))
get_path_list = get_getter(consts.path_indices, lambda i: i)
get_args_list = get_getter(consts.args_indices, lambda i: int(i))

path_list = get_path_list(0)

empty_args_aggr = numpy.zeros(len(consts.args_indices)),
empty_set = set()

args_aggr = [empty_args_aggr] * 4
link_aggr = [set(), set(), set(), set(), set()]

def create_directory(path):
    aggr = ''

    for elem, formatter in zip([consts.gen_path] + path, consts.format_folder_names):
        aggr += formatter(elem) + '/'

        if not os.path.isdir(aggr):
            os.mkdir(aggr)

    return aggr

def write_template(path, args):
    f = open(path + "index.html", 'w')
    f.write('This is test\n' + str(args))


def process_single(new_path, row):
    global path_list, args_aggr, link_aggr

    args_list = get_args_list(row)

    for i in reversed(range(4)):
        if path_list[i] == new_path[i]: break
        write_template(create_directory(path_list[:i+1]), [args_aggr[i], link_aggr[i + 1]])
        args_aggr[i] = empty_args_aggr
        link_aggr[i + 1] = set()

    for i in range(4): args_aggr[i] += numpy.asarray(args_list)
    for i in range(4): link_aggr[i].add(consts.format_folder_names[i](new_path[i]))

    path_list = new_path
    print(args_aggr, link_aggr)

# write_template(create_directory(path_list), [])

for i in range(14): process_single(get_path_list(i), i)
process_single(['', '', '', '', ''], i)

# print(args_aggr, link_aggr)

# settings.configure()
#
# ### musi się validować w pylint
# ### mogłoby w mypy
#
# e = Engine(dirs=["."])
#
# t = e.from_string("""
# {% block b1 %}
# Szablon
# {{zmienna}}
# {% for i in lista \
# %} {{i}}
# {% endfor %}
# {% endblock %}
# """)
#
# c = Context(configuration)
#
# s = t.render(c)
# # print(s)
#
# def f(x:str):
#     print(x)
#
# # f(10)
