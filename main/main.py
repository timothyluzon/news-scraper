import os;
import requests;
import json;
from bs4 import BeautifulSoup;

def get_feed(url: str):
    res = requests.get(url)
    if (res.status_code == 200):
        print(f'{res.status_code} : OK!')
        return(res.text)
    else:
        print(f'{res.status_code}')
        print(f'Feed Not Obtained from {url}')

def parse_feed(feed, max_items=5):
    soup = BeautifulSoup(feed, 'xml')
    print(soup.title)
    for _, item in zip(range(max_items), soup.find_all('item')):
        print(item.title.string)
        print(item.description.string)
        print('\n')

def main():
    print("Hello, World!")

    print(os.getcwd())
    cwd = os.getcwd()
    print(os.listdir(cwd))
    fp = os.path.join(cwd, "main/API.json")
    print(fp)
    if os.path.exists(fp):
        print(f"{fp} found")
        with open(fp, 'r') as file:
            data = json.load(file)
        URL = (data["url"])
        KEY = (data["key"])
        print(f"url: {URL}, key: {KEY}")

    else:
        print(f"{fp} not found")
    # url = 'https://www.nrk.no/rogaland/toppsaker.rss'
    # feed = get_feed(url)
    # parse_feed(feed, 3)


    #with open('db.json', 'r') as file:
    #    data = json.load(file)
    #print(data)

if __name__ == "__main__":
    main()