import json
from src.decorators import logger_utils


@logger_utils
def input_json(file_json):
    """
    Читает JSON-файл и возвращает список словарей с данными о финансовых транзакциях.

    Args:
        file_json (str): Путь к JSON-файлу

    Returns:
        list: Список словарей с данными или пустой список в случае ошибки
    """
    try:
        with open(file_json, "r", encoding="utf-8") as file:
            data = json.load(file)

        # Проверяем, что данные являются списком
        if not isinstance(data, list):
            logger_utils.error("Данные в файле не являются списком")
            return []

        logger_utils.info("Файл успешно загружен")
        return data

    except FileNotFoundError:
        logger_utils.error(f"Файл {file_json} не найден")
        return []
    except json.JSONDecodeError as e:
        logger_utils.error(f"Ошибка декодирования JSON: {e}")
        return []
    except Exception as e:
        logger_utils.error(f"Неожиданная ошибка: {e}")
        return []
