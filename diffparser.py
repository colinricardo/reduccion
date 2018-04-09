import os
import requests
from urllib.parse import quote_plus
from os.path import join, dirname

ARTICLE_API = 'https://api.diffbot.com/v3/article?url={}&token={}&discussion=false'


class ArticleAPI:
    def __init__(self, token):
        print('token --> ', token)
        self.token = token
        self._session = requests.Session()

    def parse(self, url):
        print('url received by diff parser --> ', url)
        encoded = quote_plus(url)
        r = self._session.get(ARTICLE_API.format(encoded, self.token))
        print('diff response --> ', r)
        p = Article.from_dict(r.json(), parser=self)
        print('article title --> ', p.title)
        return p


class Article:
    def __init__(self, parser):
        self._parser = parser

        self.pageUrl = None
        self.date = None
        self.author = None
        self.siteName = None
        self.videos = None
        self.title = None
        self.html = None
        self.text = None
        self.tags = None
        self.publisherCountry = None

    @classmethod
    def from_dict(clss, d, parser):
        # print('diff json -->', d)
        p = clss(parser=parser)

        objects = d['objects'][0]
        date = objects.get('date')
        author = objects.get('author')
        siteName = objects.get('siteName')
        videos = objects.get('videos')
        title = objects.get('title')
        html = objects.get('html')
        text = objects.get('text')
        tags = objects.get('tags')
        publisherCountry = objects.get('publisherCountry')

        p.date = date
        p.author = author
        p.siteName = siteName
        p.videos = videos
        p.title = title
        p.html = html
        p.text = text
        p.tags = tags
        p.publisherCountry = publisherCountry

        return p
