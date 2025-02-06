import requests
from bs4 import BeautifulSoup

def request():
    response = requests.get('https://www.nrk.no/rogaland/toppsaker.rss')
    return response

def main():
    nrk = request()
    print(nrk)
    
    soup = BeautifulSoup(nrk.content, 'xml')
    # print(soup.prettify())

    titles = soup.find_all('title')
    for title in titles:
        print(title.text)
    # print("Hello, World!")

if __name__ == "__main__":
    main()