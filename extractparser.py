import os
import requests
from urllib.parse import quote_plus
from os.path import join, dirname

EXTRACT_API = 'https://api.embedly.com/1/extract?key={}&url={}'


class ExtractAPI:
    def __init__(self, token):
        print('token --> ', token)
        self.token = token
        self._session = requests.Session()

    def parse(self, url):
        print('url received by extract parser --> ', url)
        encoded = quote_plus(url)
        r = self._session.get(EXTRACT_API.format(self.token, encoded))
        print('extract response --> ', r)
        p = Article.from_dict(r.json(), parser=self)
        print('article title --> ', p.title)
        return p


class Article:
    def __init__(self, parser):
        self._parser = parser
        self.provider = None
        self.title = None
        self.content = None

    @classmethod
    def from_dict(clss, d, parser):
        # print('diff json -->', d)
        p = clss(parser=parser)

        title = d.get('title')
        content = d.get('content')
        provider = d.get('provider_name')

        p.title = title
        p.content = content
        p.provider = provider

        return p
