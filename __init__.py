import requests
from bs4 import BeautifulSoup
from config import RSSConfig

class RSSCrawler:
    """
    Fetch RSS Feeds and restruct to news format dictionary.
    """
    config = RSSConfig()

    @classmethod
    def get(cls, newspaper):
        """
        Run whole crawl and parse process.
        """
        soup = __fetch(cls.config.links[newspaper])
        return __extract(soup, newspaper)

    @classmethod
    def __fetch(cls, rss):
        """
        Fetch XML code from RSS feed.
        """
        # TODO Clarify prerequisites for lxml
        return BeautifulSoup(requests.get(rss, headers=cls.config.req_header).text, "lxml")

    @classmethod
    def __extract(cls, soup, newspaper):
        """
        Extract news from BeautifulSoup object.
        """
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
                    #temp["content"] = clean_html(item.get_text()).strip()
                    temp["content"] = item.get_text().strip()
                else: 
                    temp[item.name] = item.string
            ret.append(temp)
        return ret
    
    @classmethod
    def __clean_html(cls, raw_html):
        """
        Utility function for replace HTML tags from string.
        """
        cleanr = re.compile('<.*?>')
        clean_text = re.sub(cleanr, '', raw_html)
        return clean_text