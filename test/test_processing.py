import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest


from src.processing import filter_by_state
from src.processing import sort_by_date


def test_filter_by_state(testing_data_operation):
    data_ex: list[dict] = filter_by_state(testing_data_operation)
    data_cancl: list[dict] = filter_by_state(testing_data_operation, state="CANCELED")
    ids_ex = [id_["id"] for id_ in data_ex]
    ids_cancl = [id_["id"] for id_ in data_cancl]
    assert ids_ex == [939719570, 142264268, 873106923, 895315941]
    assert ids_cancl == [594226727]

def test_sort_by_date():
    # Исходные данные
    operations = [
        {'amount': 100, 'date': '2023-08-01'},
        {'amount': 200, 'date': '2023-07-15'},
        {'amount': 50, 'date': '2023-08-10'}
    ]
    # Ожидаемый результат при сортировке по дате по убыванию (reverse=True)
    expected_desc = [
        {'amount': 50, 'date': '2023-08-10'},
        {'amount': 100, 'date': '2023-08-01'},
        {'amount': 200, 'date': '2023-07-15'}
    ]

    # Ожидаемый результат при сортировке по дате по возрастанию (reverse=False)
    expected_asc = [
        {'amount': 200, 'date': '2023-07-15'},
        {'amount': 100, 'date': '2023-08-01'},
        {'amount': 50, 'date': '2023-08-10'}
    ]

    # Тест по убыванию
    result_desc = sort_by_date(operations, reverse=True)
    assert result_desc == expected_desc

    # Тест по возрастанию
    result_asc = sort_by_date(operations, reverse=False)
    assert result_asc == expected_asc