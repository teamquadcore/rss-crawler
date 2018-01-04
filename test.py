from crawler.rss import RSSCrawler
from crawler.github import GithubCrawler
from crawler.config import RSSConfig
import json

# RSS test
rss_result = RSSCrawler("Engadget")
print(json.dumps(rss_result, indent=4))

# Github test
#github_result = GithubCrawler("harrydrippin")
#print(json.dumps(github_result, indent=4))