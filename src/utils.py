import json


def input_json(file_json):
    """
    Это определение функции input_json,
    которая принимает  аргумент: file_json (файл с данными о финансовых транзакциях)
    и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден,
    функция возвращает пустой список.
    """
    try:
        with open(file_json, "r", encoding="utf-8") as file:
            content = file.read()
            if "[" not in content and "]" not in content:
                print("Файл не содержит списков")
                empty_list = []
                return empty_list
            else:
                with open(file_json, encoding="utf-8") as f:
                    data = json.load(f)
                    print("Файл со списками")
                return data
    except FileNotFoundError:
        empty_list = []
        print("Файл не найден")
        return empty_list
    except json.JSONDecodeError:
        print("Ошибка декодирования JSON")
        return []