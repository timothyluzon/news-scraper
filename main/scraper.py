import requests
from bs4 import BeautifulSoup

"""
Scraper Module:
Tasks:
    1. Scrape RSS feed
        1.1. Get the RSS feed
        1.2. Extract relevant data
        1.3. Store in useful format
    2. Pass on scraped data
"""

# 1.1
# request the rss feed from news site
def request(url: str):
    response = requests.get(url)
    return response

# 1.2
def rss_parser(rss):
    soup = BeautifulSoup(rss.content, 'xml')
    items = soup.find_all('item')
    return items