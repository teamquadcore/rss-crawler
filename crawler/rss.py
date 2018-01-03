import requests
from bs4 import BeautifulSoup
from crawler import Crawler
from crawler.config import RSSConfig

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
        return [RSSConfig.links[source]]
    
    @classmethod
    def extract(cls, objs, options):
        """
        Extract news from BeautifulSoup object.
        """
        # TODO Optimize to each newspaper style
        soup = objs[0]
        ret = list()
        for entry in soup.findAll("entry"):
            temp = dict()
            for item in entry.children:
                # print(item.name)
                if item.name == None: 
                    continue
                elif item.name == "link":
                    temp["link"] = item["href"]
                elif item.name == "author":
                    temp["author"] = item.get_text().strip()
                elif item.name == "content":
                    temp["content"] = item.get_text().strip()
                else: 
                    temp[item.name] = item.string
            ret.append(temp)
        return ret