from src.masks import get_mask_card_number
from src.masks import get_mask_account
import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


@pytest.mark.parametrize("card_number, result", [
    ('676788999889989', 'Введен некорректный номер'),
    ('1241234454566556', '1241 23** **** 6556'),
    ('676788999889989', 'Введен некорректный номер'),
])
def test_get_mask_card_number(card_number, result):
    assert get_mask_card_number(card_number) == result


# Тест с правильными строками и числами
def test_get_mask_account():
    assert get_mask_account("123456789") == "**6789"
    assert get_mask_account(987654) == "**7654"
    assert get_mask_account("9876") == "**9876"
    assert get_mask_account(1234) == "**1234"

# Тест с некорректными номерами
    assert get_mask_account("123") == "Введен некорректный номер"
    assert get_mask_account("") == "Введен некорректный номер"

# Тест с некорректными типами данных
    assert get_mask_account(None) == "Введен некорректный номер"
    assert get_mask_account([1234]) == "Введен некорректный номер"
    assert get_mask_account({'num': 1234}) == "Введен некорректный номер"
