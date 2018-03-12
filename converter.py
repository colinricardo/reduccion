import os

from os.path import join, dirname
from parser import ParserAPI
from html2text import html2text
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path);

mercury = ParserAPI(api_key=os.environ.get('MERCURY_API_KEY'))

def convert(html, title=None):
  if title:
    title = '# {}'.format(title)
    html = '\n\n'.join([title, html])

  return html2text(html)

def markdown(url):
  try:
    d = mercury.parse(url)
    return convert(d.content, title=d.title)
  except KeyError:
    return None
