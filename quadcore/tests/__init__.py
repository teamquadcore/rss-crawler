from quadcore.config import Config
from quadcore.crawler.rss import RSSCrawler
from quadcore.crawler.github import GithubCrawler
import unittest
import requests

class TestRSSCrawler(unittest.TestCase):
    """
    Testcase for RSSCrawler.
    """
    def setUp(self):
        self.feed_list = Config.rss_links.keys()
        self.props = Config.rss_props

    def test_links_are_available(self):
        """
        Test for news RSS feed links.
        This test passes when all rss feed links are available.
        """
        for newspaper in self.feed_list:
            response = requests.get(Config.rss_links[newspaper], headers=Config.req_header)
            response.raise_for_status()
    
    def test_rss_crawl(self):
        """
        Test for crawling rss feeds.
        This test passes when all feed returns one or more articles.
        """
        for newspaper in self.feed_list:
            rss_result = RSSCrawler(newspaper)
            self.assertTrue(len(rss_result) >= 1)

class TestGitHubCrawler(unittest.TestCase):
    """
    Testcase for GithubCrawler.
    """
    def test_getting_profile(self):
        """
        Test for crawling Github profiles.
        This test passes when nickname and repositories are successfully parsed.
        """
        # TODO Generalize test case
        profile = GithubCrawler("harrydrippin")
        self.assertFalse(
            profile["user"]["nickname"] == "" 
            or profile["user"]["nickname"] == None
        )
        self.assertTrue(type(profile["repos"]) == type(list()))
        self.assertTrue(len(profile["repos"]) >= 1)