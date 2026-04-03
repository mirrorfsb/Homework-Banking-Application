import json
import logging
import re
from typing import Any, Dict, List

import numpy

logger = logging.getLogger("utils")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("../logs/utils.log", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def load_transactions(file_path: str) -> List[Dict[str, Any]]:
    """
    Загружает список транзакций из JSON-файла.
    Возвращает пустой список, если файл не найден, пустой,
    содержит не список или файл повреждён.
    """
    logger.info("Открываем список транзакций")
    try:
        with open(file_path, encoding="utf-8") as file:
            data = json.load(file)
            logger.info("Проверяем список или нет")
            if isinstance(data, list):
                logger.info("Загрузка списка")
                return data
            else:
                logger.error("Данные не являются списком. Вернем пустой список.")
                return []
    except (FileNotFoundError, json.JSONDecodeError) as error:
        logger.error(f"Произошла ошибка: {error}. Вернем пустой список.")
        return []


def filter_transactions_by_description(transactions, search_string):
        """Фильтрует транзакции по описанию."""

        pattern = re.compile(re.escape(search_string), re.IGNORECASE)
        return [transaction for transaction in transactions if pattern.search(transaction['description'])]


def count_operations_by_category(transactions, categories):
        """Считает количество операций по категориям."""
        category_count = {category: 0 for category in categories}
        for transaction in transactions:
            for category in categories:
                if category in transaction['description']:
                    category_count[category] += 1
        return category_count


def extract_values_transactions(data, key):
    """
    Функция принимает список словарей с данными о банковских операциях и значение ключа,
    а возвращает список категорий операций (Категории операций из поля 'description')
    """
    # Собираем все значения в список
    transactions = [item['description'] for item in data if 'description' in item]

    # Удаляем пустые значения из списка
    cleaned_category_operations = [transaction for transaction in transactions if transaction is not numpy.nan]


    # Возвращаем уникальные значения с помощью множества
    return list(set(cleaned_category_operations))

if __name__ == "__main__":

    result = load_transactions("../data/operations.json")
    print(result)
