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

ENGINE = Engine(dirs=["."])

TEMPLATE = open(consts.TEMPLATE_PATH, 'r').read()
HTML_TEMPLATE = ENGINE.from_string(TEMPLATE)

MAKE_FIELD = lambda pole: """<td>""" + str(pole) + """</td>"""

MAKE_LINK = lambda path, title: '<li><a href="' + path + '/index.html">' + str(title) + '</a></li>'
MAKE_PROC = lambda num: str(100 * num)[:config.PROC_PRECISION] + ' %'


def create_webpage(args, link, pathdata):
    [uprawnieni, wydane, oddane, niewazne, wazne] = args[:5]

    kandydaci = list(map(MAKE_FIELD, consts.KANDYDACI))
    glosy = list(map(MAKE_FIELD, args[5:]))
    wszystkie = sum(args[5:])
    procenty = list(map(lambda x: MAKE_FIELD(MAKE_PROC(x / wszystkie)), args[5:]))

    wyniki = ''
    for a, b, c in zip(kandydaci, glosy, procenty):
        wyniki += """<tr>""" + a + b + c + """</tr>"""


    # [subdirlist, subpath] = pathdata
    [subdirlist] = pathdata

    path_index = len(subdirlist) + 1
    linker = lambda sub: MAKE_LINK(
        consts.FORMAT_FOLDER_NAMES[path_index](sub), consts.FORMAT_BUTTON_NAMES[path_index](sub))

    links = '<nav class="content"><ul>'
    for a in map(linker, sorted(link)):
        links += a
    links += "</ul></nav>"

    style_path = ('../' * (len(subdirlist) - 1)) + consts.STYLESHEET_NAME

    print(pathdata)

    c = Context({
        'uprawnieni': uprawnieni,
        'wydane': wydane,
        'oddane': oddane,
        'wazne': wazne,
        'niewazne': niewazne,
        'wyniki': mark_safe(wyniki),
        'style_path': style_path,
        'frekwencja': MAKE_PROC((wazne + niewazne) / uprawnieni),
        'args': args,
        'links': mark_safe(links),
    })

    return HTML_TEMPLATE.render(c)
