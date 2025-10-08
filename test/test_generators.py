from src.generators import filter_by_currency
from src.generators import transaction_descriptions
from src.generators import card_number_generator
import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def test_filter_by_currency_basic_usd():
    transactions = [
        {"operationAmount": {"currency": {"code": "USD"}}, "id": 1},
        {"operationAmount": {"currency": {"code": "EUR"}}, "id": 2},
        {"operationAmount": {"currency": {"code": "USD"}}, "id": 3},
        {"operationAmount": {"currency": {"code": "RUB"}}, "id": 4},
    ]

    expected = [transactions[0], transactions[2]]

    result = list(filter_by_currency(transactions, "USD"))
    assert result == expected


def test_filter_by_currency_no_matches():
    transactions = [
        {"operationAmount": {"currency": {"code": "EUR"}}, "id": 10},
        {"operationAmount": {"currency": {"code": "RUB"}}, "id": 11},
    ]

    result = list(filter_by_currency(transactions, "USD"))
    assert result == []


def test_filter_by_currency_empty_input():
    empty_transactions = []

    result = list(filter_by_currency(empty_transactions, "USD"))
    assert result == []


def test_filter_by_currency_ignores_passed_argument():
    transactions = [
        {"operationAmount": {"currency": {"code": "USD"}}, "id": 100},
        {"operationAmount": {"currency": {"code": "EUR"}}, "id": 101},
    ]

    usd_result = list(filter_by_currency(transactions, "USD"))
    eur_result = list(filter_by_currency(transactions, "EUR"))

    assert usd_result == eur_result == [transactions[0]]


@pytest.mark.parametrize(
    "transactions, expected",
    [
        (
            [
                {"id": 1, "description": "Кофе"},
                {"id": 2, "description": "Обед"},
                {"id": 3, "description": "Книга"},
            ],
            ["Кофе", "Обед", "Книга"],
        ),
        (
            [
                {"id": 1, "description": "Тест"},
                {"id": 2},
                {"id": 3, "description": ""},
            ],
            ["Тест", "", ""],
        ),
        (
            [
                {"id": 1, "description": None},
                {"id": 2, "description": "Есть"},
            ],
            [None, "Есть"],
        ),
        ([], []),
    ],
)
def test_transaction_descriptions(transactions, expected):
    """Проверяем, что генератор выдаёт ровно то, что ожидается."""
    result = list(transaction_descriptions(transactions))
    assert result == expected


def test_order_is_preserved():
    """Проверяем, что порядок элементов сохраняется."""

    data = [
        {"description": "first"},
        {"description": "second"},
        {"description": "third"},
    ]
    gen = transaction_descriptions(data)
    assert next(gen) == "first"
    assert next(gen) == "second"
    assert next(gen) == "third"
    with pytest.raises(StopIteration):
        next(gen)


def test_generator_empty_range():
    gen = card_number_generator(10, 5)  # start > stop
    result = list(gen)
    assert result == []
