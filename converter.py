import os

from os.path import join, dirname
from diffbot import DiffbotAPI
import html2text
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

diff = DiffbotAPI(os.environ.get('DIFFBOT_TOKEN'))

h = html2text.HTML2Text()

h.body_width = 0 # to avoid cutting off links

def convert(html, title=None):
  if title:
    title = '# {}'.format(title)
    html = '<br>\n\n'.join([title, html])
  return h.handle(html)

def markdown(url):
  try:
    d = diff.parse(url)
    return convert(d.html, title=d.title)
  except KeyError:
    raise Exception
    return None
