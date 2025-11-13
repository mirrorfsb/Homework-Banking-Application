import os

import requests
from dotenv import load_dotenv

load_dotenv()


def get_convert_sum(transaction: dict) -> float:
    """Функция для конвертации валюты"""
    url = "https://api.apilayer.com/exchangerates_data/convert"

    payload = {
        "amount": transaction["operationAmount"]["amount"],
        "from": transaction["operationAmount"]["currency"]["code"],
        "to": "RUB"
    }

    api_key = os.getenv("API_KEY")
    headers = {"apikey": api_key}

    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        return float(transaction["operationAmount"]["amount"])
    else:
        response = requests.get(url, headers=headers, params=payload)
        result = response.json()
        return float(result["result"])
