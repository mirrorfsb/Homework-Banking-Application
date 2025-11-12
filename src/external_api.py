import os

import requests



def convert_currency(amount, currency):
    """
    Это определение функции convert_currency,
    которая принимает два аргумента: amount (сумма для конвертации)
    и currency (валюта, из которой нужно сконвертировать).
    """
    api_key = os.getenv("API_KEY")
    url = (
        f"https://api.apilayer.com/exchangerates_data-api/convert?access_key={api_key}"
        f"&from={currency}&to=RUB&amount={amount}"
    )

    response = requests.get(url)
    data = response.json()

    return data["result"]

def process_transaction(file_json):
    amount = file_json["amount"]
    currency = file_json["currency"]

    if currency in ["USD", "EUR"]:
        amount_rub = convert_currency(amount, currency)
    else:
        amount_rub = amount

    return amount_rub