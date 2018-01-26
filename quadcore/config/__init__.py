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

    # Wiki Url
    wiki_url = "https://tools.wmflabs.org/enwp10/cgi-bin/list2.fcgi?run=yes&projecta=%s&limit=1000&offset=%d&sorta=Article+title&sortb=Quality"

    # RSS feed links
    rss_links = {
        "ArsTechnica": "http://feeds.arstechnica.com/arstechnica/technology-lab",
        "Barron’s": "http://blogs.barrons.com/techtraderdaily/feed/",
        "BBCNews": "http://feeds.bbci.co.uk/news/technology/rss.xml",
        "BusinessInsider": "http://feeds.feedburner.com/typepad/alleyinsider/silicon_alley_insider",
        "CNET": "http://www.cnet.com/rss/news",
        "Computerworld": "http://www.computerworld.com/index.rss",
        "DailyExpress": "http://feeds.feedburner.com/daily-express-tech",
        "Engadget": "https://www.engadget.com/rss.xml",
        "FreeTechnologyforTeachers": "http://feeds.feedblitz.com/freetech4teachers",
        "HowToGeek": "http://feeds.howtogeek.com/HowToGeek",
        "HuffingtonPost": "http://www.huffingtonpost.com/feeds/verticals/technology/index.xml",
        "LifeHacker": "https://lifehacker.com/rss",
        "LosAngelesTimes": "http://www.latimes.com/business/technology/rss2.0.xml",
        "MakeUseOf": "http://feeds.feedburner.com/Makeuseof",
        "Mirror": "http://www.mirror.co.uk/tech/rss.xml",
        "MITTechnologyReview": "https://www.technologyreview.com/topnews.rss",
        "ReadWrite: Smart Cities": "http://feeds.feedburner.com/SmartCitiesReadwrite",
        "Recode": "http://www.recode.net/rss/index.xml",
        "Reddit": "http://www.reddit.com/r/technology/.rss",
        "Reuters": "http://feeds.reuters.com/reuters/technologyNews",
        "Techmeme": "https://www.techmeme.com/feed.xml",
        "TechCrunch": "http://feeds.feedburner.com/TechCrunch",
        "TheAtlantic": "http://www.theatlantic.com/feed/channel/technology",
        "TheNewYorkTimes": "http://rss.nytimes.com/services/xml/rss/nyt/Technology.xml",
        "TheWashingtonPost": "http://feeds.washingtonpost.com/rss/business/technology",
        "TheVerge": "https://www.theverge.com/rss/index.xml",
        "VentureBeat": "http://feeds.feedburner.com/venturebeat/SZYF",        
        "Wired": "https://www.wired.com/feed/rss"        
    }

    # Header information for yielding User-Agent validation
    # TODO Add Referrer header if needed
    req_header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
    }
   
    # Wiki category
    wiki_category = [
        "Computing",
        "Company",
        "Computer_Security",
        "Computer_Vision",
        "Computer_animation",
        "Computer_graphics",
        "Computer_hardware",
        "Computer_networking",
        "Computer_science"
    ]