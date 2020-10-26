import requests
from bs4 import BeautifulSoup
import csv



def get_html(url):    # функция отправляет запрос и получает html код
    req = requests.get(url)
    return req.text
    

def write_csv(d):    # функция записывает данные в csv file
    with open('coinmarkcap.csv', 'a') as f:
        write = csv.writer(f)
        
        write.writerow([d['name'],
                        d['ticker'],
                        d['url'],
                        d['price']])


def get_data(html):    # функция парсит html код
    soup = BeautifulSoup(html, 'lxml')

    # в переменной tags_tr все данные которые спарсились из tbody 
    tags_tr = soup.find('table', style="table-layout:auto").find('tbody', class_='rc-table-tbody').find_all('tr')
    # print(len(tags_tr))    # 101

    # cnt = 0    # переменная для подсчета кол-ва имен/тикеров на странице
    # цикл перебирает теги tr 
    for tr in tags_tr:
        tags_td = tr.find_all('td')
        if len(tags_td) > 1:    # данное условие для обхода баннера на 11й строке таблицы            
            name_coin = tags_td[2].find('p').text
            ticker_coin = tags_td[2].find('p', color="text3").text
            url_coin = 'https://coinmarketcap.com' + tags_td[2].find('a').get('href')
            
            price_coin = tags_td[3].find('a').text
            price_clear = price_coin.replace('$', '').replace(',', '')
            # cnt += 1

            data = {'name': name_coin,
                    'ticker': ticker_coin,
                    'url': url_coin,
                    'price': price_clear}
            
            write_csv(data)
        else:
            continue



def main():
    url = 'https://coinmarketcap.com/'
    print(get_data(get_html(url)))


if __name__ == '__main__':
    main()

