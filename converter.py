# TODO: use mercury for paid medium articles

import os
import html2text
from os.path import join, dirname
from article_parser import ArticleAPI
from parser import ParserAPI
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

diff = ArticleAPI(token=os.environ.get('DIFFBOT_TOKEN'))
mercury = ParserAPI(api_key=os.environ.get('MERCURY_API_KEY'))

h = html2text.HTML2Text()

h.body_width = 0  # to avoid cutting off links


def removeDoubleTitles(md):
    lines = md.split('\n')

    fourth = lines[3]
    if fourth.startswith('#'):
        return '\n'.join(lines[2:])
    return md


def process(md):
    return removeDoubleTitles(md)


def convert(html, title=None):
    print(title)
    if title:
        title = '# {}'.format(title)
        html = '<br>\n\n'.join([title, html])
    return process(h.handle(html))


def markdown(url):
    try:
        d = diff.parse(url)

        if not d.html:
            d = mercury.parse(url)
            html = d.content
        else:
            html = d.html
        return convert(html, title=d.title)
    except KeyError:
        raise Exception
