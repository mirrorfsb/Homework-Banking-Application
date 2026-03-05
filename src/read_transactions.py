import csv

import pandas as pd


def read_file_csv(file_path: str) -> list[dict[str, str]]:
    """Функция для считывания финансовых операций из CSV - файла,
    принимает путь к файлу CSV и выдает список словарей с транзакциями.
    Если файл пустой или не существует, то функция возвращает пустой список.
    """
    try:
        with open(file_path, encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=";")
            result_csv = []
            for row in reader:
                result_csv.append(row)
            if not result_csv:
                print("Warning: Файл пустой")
            return result_csv
    except FileNotFoundError:
        print("Warning: Файл не найден")
        return []


def read_file_excel(file_path: str) -> list[dict[str, str]]:
    """Функция для считывания финансовых операций из Excel - файла,
    принимает путь к файлу Excel и выдает список словарей с транзакциями.
    Если файл пустой или не существует, то функция возвращает пустой список.
    """
    try:
        df = pd.read_excel(file_path, engine='openpyxl')
        if len(df) == 0:
            print("Warning: Файл пустой")
            return []
        result_excel = df.to_dict(orient='records')
        return result_excel
    except FileNotFoundError:
        print("Warning: Файл не найден")
        return []


if __name__ == "__main__":
    for transaction in read_file_csv("../data/transactions.csv"):
        print(transaction)
    for transaction in read_file_excel("../data/transactions_excel.xlsx"):
        print(transaction)
