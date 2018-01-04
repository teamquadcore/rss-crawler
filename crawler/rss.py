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
    def extract(cls, objs, code, options):
        """
        Extract news from BeautifulSoup object.
        """
        # TODO Optimize to each newspaper style
        soup = objs[0]
        ret = list()      

        for entry in soup.findAll(RSSConfig.item_name[code]):
            temp = dict()
            temp["category"] = list()
            for item in entry.children:
                if item.name == None:   
                    continue
                elif item.name == RSSConfig.item_publish[code]:
                    continue
                elif item.name == "title":
                    temp[item.name] = item.string
                elif item.name == RSSConfig.item_content[code]:
                    temp["content"] = item.get_text().strip()
                elif item.name == "link":
                    # Separate with and without href attribute 
                    if "href" in item:
                        temp["link"] = item["href"]
                    else:
                        temp[item.name] = item.string
                elif item.name == RSSConfig.item_author[code]:
                    temp["author"] = item.get_text().strip()
                elif item.name == "category":
                    temp["category"].append(item.string)
                else: 
                    continue
            ret.append(temp)
        return ret