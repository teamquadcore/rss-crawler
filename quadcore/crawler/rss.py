import feedparser
import json
import requests
import time

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
        Extract news from feedparser object.
        # TODO Need to remove needless texts from content like 'Read more'
        """
        feed = objs[0]
        ret = list()
        is_list_thumbnail = ""

        for entry in feed.entries:
            article = dict()
            is_list_thumbnail = entry.get('media_thumbnail', 'No thumbnail')
            article["article_key"] = None 
            article["title"] = entry.get('title', 'No title')
            article["newspaper"] = code
            article["link"] = entry.get('link', 'No link')
            article["published"] = time.strftime("%Y-%m-%dT%H:%M:%S", entry.get("published_parsed", time.gmtime()))
            article["content"] = Crawler.clean_html(entry.get('description', 'No content'))
            article["author"] = entry.get('author', 'No author')
            article["entities"] = list()
            if "tags" in entry:
                article["category"] = [i["term"] for i in entry.tags]
            else:
                article["category"] = list()            
            
            if type(is_list_thumbnail) == list: 
                article["thumbnail"] = is_list_thumbnail[0]["url"]
            else:
                article["thumbnail"] = ''           

            ret.append(article)
        return ret