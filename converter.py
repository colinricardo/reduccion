import os
import re
import html2text
from os.path import join, dirname
from dotenv import load_dotenv

from extractparser import ExtractAPI
from mercuryparser import ParserAPI
from markdown import fixImages

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

ex = ExtractAPI(token=os.environ.get('EXTRACT_KEY'))
mercury = ParserAPI(api_key=os.environ.get('MERCURY_API_KEY'))

h = html2text.HTML2Text()
h.body_width = 0
h.protect_links = True
h.mark_code = True


def convert(html, title=None):
    if title:
        title = '# {}'.format(title)

    markdown = h.handle(html)
    return fixImages(markdown)


def markdown(url):
    try:
        d = mercury.parse(url)

        if not d.content:
            d = ex.parse(url)

        html = d.content
        return convert(html, title=d.title)
    except KeyError as e:
        print(e)
        raise Exception
