import requests
from bs4 import BeautifulSoup

test_url = 'https://www.nrk.no/rogaland/toppsaker.rss'

# request the rss feed from news site
def request(url: str):
    response = requests.get(url)
    return response

# parse the rss response, return the titles and description
def rss_parser(rss):
    soup = BeautifulSoup(rss.content, 'xml')
    items = soup.find_all('item')
    return items

def main():
    response = request(test_url)
    print(response)
    
    # soup = BeautifulSoup(response.content, 'xml')

    contents = rss_parser(response)
    for content in contents:
        print(f'title: {content.title.text}')
        print(f'description: {content.description.text}')

if __name__ == "__main__":  
    main()