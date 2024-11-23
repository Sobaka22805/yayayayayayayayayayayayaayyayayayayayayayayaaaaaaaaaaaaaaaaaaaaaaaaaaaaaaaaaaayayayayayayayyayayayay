from bs4 import BeautifulSoup
import requests

print('Lesson 9: Parsing Site')

responce = requests.get('https://coinmarketcap.com/')

if responce.status_code == 200:

    item_site = BeautifulSoup(responce.text, features='html.parser')
    coins = item_site.find_all('div', {'class', 'sc-b3fc6b7-0 dzgUIj'})

    for coin in coins:
        print('coin -> ', coin)
