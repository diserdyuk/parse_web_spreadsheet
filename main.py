import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    req = requests.get(url)
    return req.text
    
def write_csv(data):
    with open('coinmarkcap_bitcoin.csv', 'a') as f:
        write = csv.writer(f)
        pass

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    








def main():
    pass


if __name__ == '__main__':
    main()
