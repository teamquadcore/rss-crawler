import requests
from bs4 import BeautifulSoup
from crawler import config
from crawler.config import RSSConfig

class Crawler:
    """
    Superclass for all crawler.
    """
    normal_options = {
        "mode": "xml"
    }

    @classmethod
    def __new__(cls, self, code, options=normal_options):
        
        processed_codes = cls.preprocess(code, options)
        soups = cls.fetch(processed_codes, options)
        return cls.extract(soups, code, options)

    @classmethod
    def fetch(cls, sources, options):
        """
        Fetch XML / HTML code from source feed.
        TODO Clarify prerequisites for lxml
        """
        ret = list()
        for source in sources:
            resp = requests.get(source, headers=config.req_header)
            if options["mode"] == "xml": ret.append(BeautifulSoup(resp.text))
            elif options["mode"] == "json": ret.append(resp.json())
            elif options["mode"] == "raw": ret.append(resp)
        return ret

    @classmethod
    def clean_html(cls, raw_html):
        """
        Utility function for replace HTML tags from string.
        """
        cleanr = re.compile('<.*?>')
        clean_text = re.sub(cleanr, '', raw_html)
        return clean_text