import feedparser
import requests

from quadcore.config import Config

class Crawler:
    """
    Superclass for all crawler.
    """
    normal_options = {
        "mode": "feed"
    }

    @classmethod
    def __new__(cls, self, code, options=normal_options):
        processed_codes = cls.preprocess(code, options)
        data_objects = cls.fetch(processed_codes, options)
        return cls.extract(data_objects, code, options)

    @classmethod
    def fetch(cls, sources, options):
        """
        Fetch XML / HTML code from source feed.
        TODO Clarify prerequisites for lxml
        """
        data_objects = list()
        for source in sources:
            resp = requests.get(source, headers=Config.req_header)
            if options["mode"] == "feed": 
                data_objects.append(feedparser.parse(resp.text))
            elif options["mode"] == "html": 
                data_objects.append(BeautifulSoup(resp.text, "lxml"))
            elif options["mode"] == "json": 
                data_objects.append(resp.json())
            elif options["mode"] == "raw": 
                data_objects.append(resp)
        return data_objects

    @classmethod
    def clean_html(cls, raw_html):
        """
        Utility function for replace HTML tags from string.
        """
        cleanr = re.compile('<.*?>')
        clean_text = re.sub(cleanr, '', raw_html)
        return clean_text