import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest


from src.widget import mask_account_card
from src.widget import get_date

@pytest.mark.parametrize(

    "card_info, expected",
    [
        # Корректные карты
        ("Visa Platinum 1234567890123456", "Visa Platinum 1234 56** **** 3456"),  #пример, предполагаемая маска
        ("Maestro 1111222233334444", "Maestro 1111 22** **** 4444"),             #пример, предполагаемая маска
        # Некорректные случаи
        ("Visa Platinum 12345678", "Некорректный ввод"),  #длина меньше 16
        ("UnknownType 1234567890123456", "Некорректный ввод"),
        ("Visa Platinum", "Некорректный ввод"),  #отсутствует номер
        ("Maestro 123", "Некорректный ввод"),  #неправильная длина
    ]
)
def test_mask_account_card(card_info, expected):
    result = mask_account_card(card_info)
    assert result == expected

@pytest.mark.parametrize(
    "input_date, expected_output",
    [
        ("2023-03-15", "15.03.2023"),             # cтандартная дата
        ("2020-02-29", "29.02.2020"),             # високосный год
        ("1999-12-31", "31.12.1999"),             # конец года
        ("2023-13-01", "Некорректный формат даты"),  # неверный месяц
        ("2023-00-10", "Некорректный формат даты"),  # неверный месяц
        ("2023-02-30", "Некорректный формат даты"),  # неверный день
        ("not-a-date", "Некорректный формат даты"), # некорректный формат
        ("2023-01-01T12:00:00", "01.01.2023"),     # с временной частью
        ("2023-13-01T12:00:00", "Некорректный формат даты"),  # неверный месяц с временной
    ],
)
def test_get_date(input_date, expected_output):
    result = get_date(input_date)
    assert result == expected_output

