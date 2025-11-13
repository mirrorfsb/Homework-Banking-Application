import json


def input_json(file_json):
    """
    Это определение функции input_json,
    которая принимает аргумент: file_json (файл с данными о финансовых транзакциях)
    и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден,
    функция возвращает пустой список.
    """
    try:
        with open(file_json, "r", encoding="utf-8") as file:
            content = file.read()

            # Проверяем, пустой ли файл
            if not content.strip():
                return []

            # Проверяем, что содержимое - это список (начинается с [ и заканчивается ])
            if not (content.strip().startswith('[') and content.strip().endswith(']')):
                return []

            data = json.load(content)

            # Проверяем, что результат - список
            if not isinstance(data, list):
                return []

            return data

    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []
