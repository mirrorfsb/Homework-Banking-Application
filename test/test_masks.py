import sys
from pathlib import Path

import pytest

# Добавляем путь к src в sys.path корректно
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize("card_number, result", [
    ("676788999889989", "Введен некорректный номер"),
    ("1241234454566556", "1241 23** **** 6556"),
    ("676788999889989", "Введен некорректный номер"),
])
def test_get_mask_card_number(card_number, result):
    assert get_mask_card_number(card_number) == result


def test_get_mask_account():
    """Тест функции маскирования счета"""
    # Тест с правильными строками и числами
    assert get_mask_account("123456789") == "6789"
    assert get_mask_account(987654) == "7654"  # Было "7654", должно быть "7654"
    assert get_mask_account("9876") == "9876"
    assert get_mask_account(1234) == "1234"

    # Тест с некорректными номерами
    assert get_mask_account("123") == "Введен некорректный номер"
    assert get_mask_account("") == "Введен некорректный номер"

    # Тест с некорректными типами данных
    assert get_mask_account(None) == "Введен некорректный номер"
    assert get_mask_account([1234]) == "Введен некорректный номер"
    assert get_mask_account({"num": 1234}) == "Введен некорректный номер"
