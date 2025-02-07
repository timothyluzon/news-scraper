import scraper

test_url = 'https://www.nrk.no/rogaland/toppsaker.rss'

def main():
    feed = scraper.request(test_url)
    articles = scraper.rss_parser(feed)

    for article in articles:
        print(article.title.text)
        print(article.description.text)

if __name__ == "__main__":  
    main()