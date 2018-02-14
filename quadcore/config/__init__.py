from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

class Config:
    # Configuration for redis
    redis = {
        "host": os.environ.get("REDIS_HOST"),
        "id": os.environ.get("REDIS_ID"),
        "password": os.environ.get("REDIS_PASSWORD"),
        "port": os.environ.get("REDIS_PORT"),
        "db": os.environ.get("REDIS_DB_NUMBER")
    }

    # Dandelion API
    dandelion_url = 'https://api.dandelion.eu/datatxt/nex/v1'
    dandelion_token = os.environ.get("DANDELION_TOKEN")
    dandelion_who = ["Henry", "Zoey", "Roy", "Harry"]

    # Wiki Url
    wiki_url = "https://tools.wmflabs.org/enwp10/cgi-bin/list2.fcgi?run=yes&projecta=%s&limit=1000&offset=%d&sorta=Article+title&sortb=Quality"

    # RSS feed links
    rss_links = {       
        "Ars Technica": "http://feeds.arstechnica.com/arstechnica/technology-lab",
        "Barron’s": "http://blogs.barrons.com/techtraderdaily/feed/",
        "BBC News": "http://feeds.bbci.co.uk/news/technology/rss.xml",
        "Business Insider": "http://feeds.feedburner.com/typepad/alleyinsider/silicon_alley_insider",
        "CNET": "http://www.cnet.com/rss/news",
        "Computerworld": "http://www.computerworld.com/index.rss",
        "Daily Express": "http://feeds.feedburner.com/daily-express-tech",
        "Engadget": "https://www.engadget.com/rss.xml",
        "Free Technology for Teachers": "http://feeds.feedblitz.com/freetech4teachers",
        "How To Geek": "http://feeds.howtogeek.com/HowToGeek",
        "Huffington Post": "http://www.huffingtonpost.com/feeds/verticals/technology/index.xml",
        "LifeHacker": "https://lifehacker.com/rss",
        "Los Angeles Times": "http://www.latimes.com/business/technology/rss2.0.xml",
        "MakeUseOf": "http://feeds.feedburner.com/Makeuseof",
        "Mirror": "http://www.mirror.co.uk/tech/rss.xml",
        "MIT Technology Review": "https://www.technologyreview.com/topnews.rss",
        "ReadWrite: Smart Cities": "http://feeds.feedburner.com/SmartCitiesReadwrite",
        "Recode": "http://www.recode.net/rss/index.xml",
        "Reddit": "http://www.reddit.com/r/technology/.rss",
        "Reuters": "http://feeds.reuters.com/reuters/technologyNews",
        "Techmeme": "https://www.techmeme.com/feed.xml",
        "TechCrunch": "http://feeds.feedburner.com/TechCrunch",
        "The Atlantic": "http://www.theatlantic.com/feed/channel/technology",
        "The New York Times": "http://rss.nytimes.com/services/xml/rss/nyt/Technology.xml",
        "The Washington Post": "http://feeds.washingtonpost.com/rss/business/technology",
        "The Verge": "https://www.theverge.com/rss/index.xml",
        "VentureBeat": "http://feeds.feedburner.com/venturebeat/SZYF",        
        "Wired": "https://www.wired.com/feed/rss"
    }

    # Header information for yielding User-Agent validation
    # TODO Add Referrer header if needed
    req_header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
    }
    