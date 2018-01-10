from quadcore.crawler.rss import RSSCrawler
from quadcore.crawler.github import GithubCrawler
from quadcore.manager.data import DataManager as dm
import json
import sys

class ManualTest:
    """
    Static class for manual test method definition.
    """

    @classmethod
    def rss(cls):
        """
        RSS crawling test for developers.
        """
        # TODO prevent from unappropriate input
        newspaper = input("[+] Newspaper name: ")
        rss_result = RSSCrawler(newspaper)
        print(json.dumps(rss_result, indent=4))

    @classmethod
    def github(cls):
        """
        GitHub crawling test for developers.
        """
        # TODO prevent from fake username
        username = input("[+] GitHub Username: ")
        github_result = GithubCrawler(username)
        print(json.dumps(github_result, indent=4))

    @classmethod
    def data(cls):
        """
        DataManager test for developers.
        """
        curr_entity = dm.get_entity_count()
        curr_article = dm.get_article_count()
        print("[+] Current Entity Count =", curr_entity)
        print("[+] Current Article Count =", curr_article)
        print("[+] Checking entity count set (True) =", 
            dm.set_entity_count(curr_entity))
        print("[+] Checking article count set (True) =", 
            dm.set_article_count(curr_article))