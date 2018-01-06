import requests
from bs4 import BeautifulSoup
from quadcore.crawler import Crawler
from quadcore.config import Config as conf

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
        return [conf.rss_links[source]]
    
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

        for entry in soup.findAll(conf.rss_props[code][ITEM_NAME]):
            article = dict()
            article["category"] = list()
            for item in entry.children:
                if item.name == None or item.name == conf.rss_props[code][ITEM_NAME]:
                    continue
                elif item.name == "title":
                    article[item.name] = item.string
                elif item.name == conf.rss_props[code][ITEM_CONTENT]:
                    article["content"] = item.get_text().strip()
                elif item.name == "link":
                    # Use "href" attribute if available
                    article["link"] = (item["href"] if (item.get("href") != None) else item.string)
                elif item.name == conf.rss_props[code][ITEM_AUTHOR]:
                    article["author"] = item.get_text().strip()
                elif item.name == "category":
                    article["category"].append(item.string)
                else: 
                    continue
            ret.append(article)
        return ret