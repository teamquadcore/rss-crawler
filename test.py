from crawler import config
from crawler.rss import RSSCrawler
from crawler.github import GithubCrawler
from crawler.config import RSSConfig as rss_conf
import unittest
import requests

class TestRSSCrawler(unittest.TestCase):
    """
    Testcase for RSSCrawler.
    """
    def setUp(self):
        self.feed_list = rss_conf.links.keys()
        self.props = rss_conf.properties

    def test_links_are_available(self):
        for newspaper in self.feed_list:
            response = requests.get(rss_conf.links[newspaper], headers=config.req_header)
            response.raise_for_status()
    
    def test_rss_crawl(self):
        for newspaper in self.feed_list:
            rss_result = RSSCrawler(newspaper)
            self.assertTrue(len(rss_result) >= 1)

class TestGitHubCrawler(unittest.TestCase):
    """
    Testcase for GithubCrawler.
    """
    def test_getting_profile(self):
        # TODO Generalize test case
        profile = GithubCrawler("harrydrippin")
        self.assertFalse(
            profile["user"]["nickname"] == "" 
            or profile["user"]["nickname"] == None
        )
        self.assertTrue(type(profile["repos"]) == type(list()))
        self.assertTrue(len(profile["repos"]) >= 1)

if __name__ == '__main__':
    unittest.main()