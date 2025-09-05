import requests;

def get_feed():
    res = requests.get('https://www.nrk.no/rogaland/toppsaker.rss')
    if (res.status_code == 200):
        print(f'{res.status_code} : OK!')

def main():
    print("Hello, World!")
    get_feed()

if __name__ == "__main__":
    main()