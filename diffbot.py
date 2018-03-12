import os
import requests
import json
from os.path import join, dirname
from dotenv import load_dotenv
import urllib.parse

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

DIFFBOT_API = os.environ.get('DIFFBOT_API')

class DiffbotAPI(object):
  def __init__(self, token):
    super(DiffbotAPI, self).__init__()
    self.token = token
    self._session = requests.Session()

  def parse(self, url):
    encodedUrl = urllib.parse.quote_plus(url)
    realUrl = DIFFBOT_API.format(encodedUrl, self.token)
    r = self._session.get(realUrl)
    p = ParsedArticle.fromDict(r.json(), parser=self)
    return p

class ParsedArticle(object):
  def __init__(self, parser):
    super(ParsedArticle, self).__init__()
    self._parser = parser

    self.url = None
    self.pageUrl = None
    self.date = None
    self.author = None
    self.siteName = None
    self.videos = None
    self.title = None
    self.html = None
    self.text = None

  def __repr__(self):
    return '<ParsedArticle url={0!r}>'.format(self.url)

  @classmethod
  def fromDict(klass, d, parser):
    p = klass(parser=parser)

    objects = d['objects'][0]
    date = objects['date']
    author = objects['author']
    siteName = objects['siteName']
    videos = objects['videos']
    title = objects['title']
    html = objects['html']
    text = objects['text']

    p.date = date
    p.author = author
    p.siteName = siteName
    p.videos = videos
    p.title = title
    p.html = html
    p.text = text
    return p