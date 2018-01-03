from crawler.rss import RSSCrawler
from crawler.config import RSSConfig
import json

rss_result = RSSCrawler("The Verge")

print(json.dumps(rss_result, indent=4))