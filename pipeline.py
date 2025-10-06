""""
Crypto Price ETL - Extract & Transform Module

This module contains the functions to extract the cryptocurrency prices from the CoinGecko API and transform them into structured records
"""""

import requests
from datetime import datetime

url = "https://api.coingecko.com/api/v3/simple/price"

def extract_prices(coin_name):
    params = {
        "ids": coin_name,
        "vs_currencies": "usd"
    }
    response = requests.get(url, params=params)

    if response.status_code == 200:
        print("Data Received")
        return response.json()
    else:
        print(f"Failed to retrieve data {response.status_code}")
        return None
extract_prices("bitcoin")

def transform_prices(raw_data):
    bitcoin_data = raw_data["bitcoin"]

    price = bitcoin_data["usd"]

    formatted_data = {
        "coin": "bitcoin",
        "price_usd": price,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    }
    return formatted_data



