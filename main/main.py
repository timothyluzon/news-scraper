import requests;
from bs4 import BeautifulSoup;

def get_feed(url: str):
    res = requests.get(url)
    if (res.status_code == 200):
        print(f'{res.status_code} : OK!')
        return(res.text)
    else:
        print(f'{res.status_code}')
        print(f'Feed Not Obtained from {url}')

def parse_feed(feed):
    soup = BeautifulSoup(feed, 'xml')
    print(soup.title)
    for item in soup.find_all('item'):
        print(item.title.string)
        print(item.description.string)
        print('\n')

def main():
    print("Hello, World!")
    url = 'https://www.nrk.no/rogaland/toppsaker.rss'
    feed = get_feed(url)
    parse_feed(feed)

if __name__ == "__main__":
    main()