import requests
from bs4 import BeautifulSoup
from crawler import config
from crawler.config import RSSConfig

class Crawler:
    """
    Superclass for all crawler.
    """
    @classmethod
    def __new__(cls, self, code, options=dict()):
        soup = cls.fetch(cls.preprocess(code))
        return cls.extract(soup, options)

    @classmethod
    def fetch(cls, source):
        """
        Fetch XML / HTML code from source feed.
        """
        # TODO Clarify prerequisites for lxml
        return BeautifulSoup(requests.get(source, headers=config.req_header).text, "lxml")

    @classmethod
    def clean_html(cls, raw_html):
        """
        Utility function for replace HTML tags from string.
        """
        cleanr = re.compile('<.*?>')
        clean_text = re.sub(cleanr, '', raw_html)
        return clean_text