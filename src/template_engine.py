"""Library responsible for putting relevant data on the page, where it's needed"""

from django.template import Context
from django.utils.safestring import mark_safe
from django.template.engine import Engine
from django.conf import settings

import consts
import config

settings.configure()

ENGINE = Engine(dirs=["."])

TEMPLATE = open(consts.TEMPLATE_PATH, 'r').read()
HTML_TEMPLATE = ENGINE.from_string(TEMPLATE)


def make_field(pole):
    return '<td>' + str(pole) + '</td>'


def make_link(path, title):
    return '<li><a href="' + path + '/index.html">' + str(title) + '</a></li>'


def make_proc(num):
    return str(100 * num)[:config.PROC_PRECISION] + ' %'


def make_button_name(path_list):
    list_len = len(path_list)
    return consts.FORMAT_BUTTON_NAMES[list_len](path_list[list_len - 1])


def make_path(path_list):
    """Creates a component with links to parent pages"""
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
    for par in reversed(out_list):
        out += par

    return out


def make_links(path_index, link):
    """Creates a component with links to subpages"""
    linker = lambda sub: make_link(
        consts.FORMAT_FOLDER_NAMES[path_index](sub), consts.FORMAT_BUTTON_NAMES[path_index](sub))

    if len(link) < 1:
        return ''

    links = '<header> <h4>Linki</h4> <hr/> </header><nav class="content"><ul>'
    for subpage in map(linker, sorted(link)):
        links += subpage
    links += "</ul></nav>"

    return links


def make_results(args):
    """Creates contents of table with election results"""
    kandydaci = list(map(make_field, consts.KANDYDACI))
    glosy = list(map(make_field, args))
    wszystkie = sum(args)
    if wszystkie <= 0: wszystkie = 1
    procenty = list(map(lambda x: make_field(make_proc(x / wszystkie)), args))

    wyniki = ''
    for kand, glos, proc in zip(kandydaci, glosy, procenty):
        wyniki += '<tr>' + kand + glos + proc + '</tr>'

    return wyniki


def create_webpage(args, link, pathdata):
    """Composes data given via arguments into an election subpage"""
    [uprawnieni, wydane, oddane, niewazne, wazne] = args[:5]

    [subdirlist] = pathdata

    path_index = len(subdirlist) + 1

    style_relative_path = ('../' * (len(subdirlist) - 1)) + consts.STYLESHEET_NAME

    contxt = Context({
        'uprawnieni': uprawnieni,
        'wydane': wydane,
        'oddane': oddane,
        'wazne': wazne,
        'niewazne': niewazne,
        'wyniki': mark_safe(make_results(args[5:])),
        'style_path': style_relative_path,
        'frekwencja': make_proc((wazne + niewazne) / uprawnieni),
        'args': args,
        'links': mark_safe(make_links(path_index, link)),
        'path': mark_safe(make_path(subdirlist))
    })

    return HTML_TEMPLATE.render(contxt)
