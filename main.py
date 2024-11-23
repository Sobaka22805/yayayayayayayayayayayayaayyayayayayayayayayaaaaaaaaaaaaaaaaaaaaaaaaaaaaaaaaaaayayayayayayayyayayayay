from bs4 import BeautifulSoup
import requests

print('Lesson 9: Parsing Site')

responce = requests.get('https://coinmarketcap.com/')

if responce.status_code == 200:

    # print('Before parser', responce.text)
    item_site = BeautifulSoup(responce.text, features='html.parser')
    coins_rates = item_site.find_all('div', {'class', 'sc-b3fc6b7-0 dzgUIj'})

    for rate in coins_rates:
        # print('Coin ->', coin)
        # print('Rate object ->', rate)
        price = float(rate.findNext().text[1:].replace(',', ''))
        print('Price ->', price)

