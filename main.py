import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):    # функция отправляет запрос и получает html код
    req = requests.get(url)
    return req.text
    

def write_csv(data):    # функция записывает данные в csv file
    with open('coinmarkcap_bitcoin.csv', 'a') as f:
        write = csv.writer(f)
        pass


def get_data(html):    # функция парсит html код
    soup = BeautifulSoup(html, 'lxml')

    # в переменной tags_tr все данные которые спарсились из tbody 
    tags_tr = soup.find('table', style="table-layout:auto").find('tbody', class_='rc-table-tbody').find_all('tr')
    # print(len(tags_tr))    # 101

    # цикл перебирает теги tr 
    for tr in tags_tr:
        tags_td = tr.find_all('td')
        # print()
        if len(tags_td) > 3:    # данное условие для обхода баннера на 11й строке таблицы            
            name_coin = tags_td[2].find('p', color="text").text
            ticker_coin = tags_td[2].find('p', color="text3").text
            print(name_coin, ticker_coin)
        else:
            continue

        



def main():
    url = 'https://coinmarketcap.com/'
    print(get_data(get_html(url)))


if __name__ == '__main__':
    main()
