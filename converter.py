import os

from os.path import join, dirname
from parser import ParserAPI
import html2text
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path);

mercury = ParserAPI(api_key=os.environ.get('MERCURY_API_KEY'))

h = html2text.HTML2Text()

h.body_width = 0 # to avoid cutting off links

def convert(html, lead_image_url=None, title=None):
  header = ''
  if title:
    if lead_image_url:
        header = '![header]({})<br><br>'.format(lead_image_url)
    title = '# {}'.format(title)
    html = '\n\n'.join([header, title, html])

  return h.handle(html)

def markdown(url):
  try:
    d = mercury.parse(url)
    return convert(d.content, lead_image_url=d.lead_image_url, title=d.title)
  except KeyError:
    raise Exception
    return None
