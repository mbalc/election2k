from django.template import Context
from django.utils.safestring import mark_safe
from django.template.engine import Engine
from django.conf import settings

import consts
import config

settings.configure()

### musi się validować w pylint/
### mogłoby w mypy

ENGINE = Engine(dirs=["."])

TEMPLATE = open(consts.TEMPLATE_PATH, 'r').read()
HTML_TEMPLATE = ENGINE.from_string(TEMPLATE)

MAKE_FIELD = lambda pole: '<td>' + str(pole) + '</td>'

MAKE_LINK = lambda path, title: '<li><a href="' + path + '/index.html">' + str(title) + '</a></li>'
MAKE_PROC = lambda num: str(100 * num)[:config.PROC_PRECISION] + ' %'

def make_button_name(path_list):
    list_len = len(path_list)
    return consts.FORMAT_BUTTON_NAMES[list_len](path_list[list_len - 1])

def make_path(path_list):
    dirs = ''
    out_list = [
        '<span>' + make_button_name(path_list) + '</span>'
    ]
    for i in reversed(range(len(path_list) - 1)):
        dirs += '../'
        name = consts.FORMAT_BUTTON_NAMES[i + 1](path_list[i])
        tag = '<a href="' + dirs + 'index.html">' + name + '</a>'
        out_list.append(' - ')
        out_list.append(tag)


    out = ''
    for elem in reversed(out_list):
        out += elem

    return out

def make_links(path_index, link):
    linker = lambda sub: MAKE_LINK(
        consts.FORMAT_FOLDER_NAMES[path_index](sub), consts.FORMAT_BUTTON_NAMES[path_index](sub))

    if len(link) < 1:
        return ''

    links = '<header> <h4>Linki</h4> <hr/> </header><nav class="content"><ul>'
    for a in map(linker, sorted(link)):
        links += a
    links += "</ul></nav>"

    return links

def make_results(args):
    kandydaci = list(map(MAKE_FIELD, consts.KANDYDACI))
    glosy = list(map(MAKE_FIELD, args))
    wszystkie = sum(args)
    procenty = list(map(lambda x: MAKE_FIELD(MAKE_PROC(x / wszystkie)), args))

    wyniki = ''
    for a, b, c in zip(kandydaci, glosy, procenty):
        wyniki += '<tr>' + a + b + c + '</tr>'

    return wyniki

def create_webpage(args, link, pathdata):
    [uprawnieni, wydane, oddane, niewazne, wazne] = args[:5]

    # [subdirlist, subpath] = pathdata
    [subdirlist] = pathdata

    path_index = len(subdirlist) + 1

    style_path = ('../' * (len(subdirlist) - 1)) + consts.STYLESHEET_NAME

    c = Context({
        'uprawnieni': uprawnieni,
        'wydane': wydane,
        'oddane': oddane,
        'wazne': wazne,
        'niewazne': niewazne,
        'wyniki': mark_safe(make_results(args[5:])),
        'style_path': style_path,
        'frekwencja': MAKE_PROC((wazne + niewazne) / uprawnieni),
        'args': args,
        'links': mark_safe(make_links(path_index, link)),
        'path': mark_safe(make_path(subdirlist))
    })

    return HTML_TEMPLATE.render(c)
