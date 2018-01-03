class RSSConfig:
    # RSS feed list
    newspaper = ["The Verge", "Engadget", "TechCrunch"]

    # RSS feed links
    links = {
        "The Verge": "https://www.theverge.com/rss/index.xml",
        "Engadget": "https://www.engadget.com/rss.xml",
        # Feedburner based XML Feed, need to be careful
        "TechCrunch": "http://feeds.feedburner.com/TechCrunch/"
    }

    # Yielding User-Agent validation
    # TODO Add Referrer header if needed
    req_header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
    }