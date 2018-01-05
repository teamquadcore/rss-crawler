import requests
from datetime import datetime
from dateutil import parser
from bs4 import BeautifulSoup
from crawler import Crawler
from crawler.config import RSSConfig as conf

class RSSCrawler(Crawler):
    """
    Fetch RSS Feeds and restruct to news format dictionary.
    """

    @classmethod
    def preprocess(cls, source, options):
        """
        Preprocess source to proper URL string.
        Returns list of urls to fetch.
        """
        return [conf.links[source]]
    
    @classmethod
    def extract(cls, objs, code, options):
        """
        Extract news from BeautifulSoup object.
        # TODO Need to extract needless texts from content like 'Read more'
        """
        # constant numbers for property index
        ITEM_NAME = 0
        ITEM_PUBLISH = 1
        ITEM_CONTENT = 2
        ITEM_AUTHOR = 3
        
        soup = objs[0]
        ret = list()      

        for entry in soup.findAll(conf.properties[code][ITEM_NAME]):
            article = dict()
            article["category"] = list()
            article["keywords"] = list()
            for item in entry.children:
                if item.name == None: 
                    continue
                elif item.name == conf.properties[code][ITEM_PUBLISH]:
                    article["publish_date"] = cls.parse_date(item.string)
                elif item.name == "title":
                    article[item.name] = item.string
                elif item.name == conf.properties[code][ITEM_CONTENT]:
                    article["content"] = cls.parse_content(item.get_text().strip())
                elif item.name == "link":
                    # Use "href" attribute if available
                    article["link"] = (item["href"] if (item.get("href") != None) else item.string)
                elif item.name == conf.properties[code][ITEM_AUTHOR]:
                    article["author"] = item.get_text().strip()
                elif item.name == "category":
                    article[item.name].append(item.string)
                elif item.name == "keywords":
                    article[item.name].append(item.string)
                else: 
                    continue
            ret.append(article)
        return ret

    @classmethod
    def parse_date(cls, date_string):
        new_date = parser.parse(date_string)
        new_date_string = str(new_date) 
        return new_date_string

    @classmethod
    def parse_content(cls, content_string):
        new_content_string = content_string.split("Read more...")[0]
        return new_content_string