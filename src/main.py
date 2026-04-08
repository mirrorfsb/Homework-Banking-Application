from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.read_transactions import read_file_csv, read_file_excel
from src.utils import extract_values_transactions, filter_transactions_by_description, load_transactions
from src.widget import get_date, mask_account_card

if __name__ == '__main__':

    def main():
        """Отвечает за основную логику проекта и связывает функциональности между собой"""
        transaction_data = []
        while True:
            print(
                """
            Программа: Привет! Добро пожаловать в программу работы
            с банковскими транзакциями.
            Выберите необходимый пункт меню:
            1. Получить информацию о транзакциях из JSON-файла
            2. Получить информацию о транзакциях из CSV-файла
            3. Получить информацию о транзакциях из XLSX-файла
            """
            )
            users_input = int(input("Введите нужную цифру:\n"))
            if users_input in [1, 2, 3]:
                break

        if users_input == 1:
            print("Программа: Для обработки выбран JSON-файл.")
            transaction_data = load_transactions("../data/operations.json")
        elif users_input == 2:
            print("Программа: Для обработки выбран CSV-файл.")
            transaction_data = read_file_csv("../data/transactions.csv")
        elif users_input == 3:
            print("Программа: Для обработки выбран XLSX-файл.")
            transaction_data = read_file_excel("../data/transactions_excel.xlsx")

        print(
            """
            Программа: Введите статус, по которому необходимо выполнить фильтрацию.
            Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
            """
        )

        while True:
            users_input_1 = input("Введите статус:\n").strip().upper()
            if users_input_1 in ["EXECUTED", "CANCELED", "PENDING"]:
                print(f"Программа: Операции отфильтрованы по статусу {users_input_1}")
                break
            print(f"Программа: Статус операции {users_input_1} недоступен.\n"
                   "Программа: Введите статус, по которому необходимо выполнить фильтрацию.\n"
                   "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")

        # Фильтрация транзакций по статусу
        transaction_data = filter_by_state(transaction_data, state=users_input_1)

        # Сортировка по дате
        users_input_date = input("Программа: Отсортировать операции по дате? "
                                 "Да/Нет, или любую клавишу\n").strip().upper()
        if users_input_date in ['ДА', 'YES']:
            users_input_data = input("Программа: Отсортировать по возрастанию/по убыванию?\n").strip().lower()
            if users_input_data == 'по возрастанию':
                transaction_data = sort_by_date(transaction_data, descending=False)
            elif users_input_data == 'по убыванию':
                transaction_data = sort_by_date(transaction_data, descending=True)

        # Фильтрация транзакций по валюте
        users_input_currency = input("Программа: Выводить только рублевые транзакции? "
                                     "Да/Нет, или любую клавишу\n").strip().upper()
        if users_input_currency in ['ДА', 'YES']:
            if users_input == 1:
                transaction_data = filter_by_currency(transaction_data)
            elif users_input in [2, 3]:
                transaction_data = filter_by_currency(transaction_data)

        users_input_descript = input("Отфильтровать список транзакций по определенному слову в описании? "
                                     "Да/Нет, или любую клавишу\n").strip().upper()
        if users_input_descript in ['ДА', 'YES']:
            filter_word = extract_values_transactions(transaction_data, key='description')
            users_input_descript_1 = input(f"Программа: Введите слово для фильтрации.\n "
                                           f"Возможные варианты{filter_word}\n")
            transaction_data = filter_transactions_by_description(transaction_data, users_input_descript_1)

        # Вывод результатов
        if len(transaction_data) == 0:
            print("Программа: Не найдено ни одной транзакции, "
                  "подходящей под ваши условия фильтрации")
        else:
            print(f"Программа: Распечатываю итоговый список транзакций\n"
                  f"Программа: Всего банковских операций в выборке: {len(transaction_data)}")
            for i in transaction_data:
                d_i = i.get("date")
                data_i = get_date(d_i)
                from_i = i.get("from", '')
                to_i = i.get("to", '')
                if users_input == 1:
                    currency_i = i.get("operationAmount", {}).get("currency", {}).get("code")
                    amount_i = i.get("operationAmount", {}).get("amount")
                else:
                    currency_i = i.get("currency_code")
                    amount_i = i.get("amount")
                print(f"""
                            {data_i} {i.get('description')}
                            {mask_account_card(from_i)} - > {mask_account_card(to_i)}
                            Сумма: {amount_i}  {currency_i}
                  """)

    if __name__ == "__main__":
        main()
