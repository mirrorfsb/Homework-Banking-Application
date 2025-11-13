import os
from unittest.mock import patch

from src.external_api import get_convert_sum

# Имитация транзакции
sample_transaction = {
    "operationAmount": {
        "amount": "25",
        "currency": {
            "code": "GBP"
        }
    }
}


@patch('requests.get')
def test_get_convert_sum(mock_get):
    # Подготавливаем моковое значение для response.json()
    mock_get.return_value.json.return_value = {
        "date": "2018-02-22",
        "historical": "",
        "info": {
            "rate": 148.972231,
            "timestamp": 1519328414
        },
        "query": {
            "amount": 25,
            "from": "GBP",
            "to": "RUB"
        },
        "result": 3724.305775
    }

    # Задаём API-KEY
    os.environ["API_KEY"] = "FAKE_API_KEY"

    # Вызываем функцию
    result = get_convert_sum(sample_transaction)

    # Проверяем результат
    assert result == 3724.305775

    # Проверяем, что вызов был осуществлён с правильными параметрами
    mock_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert",
        headers={"apikey": "FAKE_API_KEY"},
        params={
            "amount": "25",
            "from": "GBP",
            "to": "RUB"
        }
    )
