from Tools.scripts.treesync import create_directories

from django.template import Context
from django.utils.safestring import mark_safe
from django.template.engine import Engine
from django.conf import settings

import consts
import config

# print(args_aggr, link_aggr)

settings.configure()

### musi się validować w pylint/
### mogłoby w mypy

e = Engine(dirs=["."])

template = open(consts.template_path, 'r').read()
t = e.from_string(template)

make_field = lambda pole: """<td>""" + str(pole) + """</td>"""

make_link = lambda path, title: '<li><a href="' + path + '/index.html">' + str(title) + '</a></li>'
make_proc = lambda num: str(100 * num)[:config.proc_precision] + ' %'


def create_webpage(args, link, pathdata):
    [uprawnieni, wydane, oddane, niewazne, wazne] = args[:5]

    kandydaci = list(map(make_field, consts.kandydaci))
    glosy = list(map(make_field, args[5:]))
    wszystkie = sum(args[5:])
    procenty = list(map(lambda x: make_field(make_proc(x / wszystkie)), args[5:]))

    wyniki = ''
    for a, b, c in zip(kandydaci, glosy, procenty):
        wyniki += """<tr>""" + a + b + c + """</tr>"""


    [subdirlist, subpath] = pathdata

    path_index = len(subdirlist) + 1
    linker = lambda sub: make_link(
        consts.format_folder_names[path_index](sub), consts.format_button_names[path_index](sub))

    links = "<nav><ul>"
    for a in map(linker, sorted(link)):
        links += a
    links += "</ul></nav>"

    style_path = ('../' * (len(subdirlist) - 1)) + consts.stylesheet_name

    print(pathdata)

    c = Context({
        'uprawnieni': uprawnieni,
        'wydane': wydane,
        'oddane': oddane,
        'wazne': wazne,
        'niewazne': niewazne,
        'wyniki': mark_safe(wyniki),
        'style_path': style_path,
        'frekwencja': make_proc((wazne + niewazne) / uprawnieni),
        'args': args,
        'links': mark_safe(links),
    })

    return t.render(c)
