def filter_by_state(banking_operations: list, state: str = 'EXECUTED') -> list:
    """ Функция принимает на вход список словарей с данными о банковских операциях и параметр state,
    возвращает новый список, содержащий только те словари,
    у которых ключ state содержит переданное в функцию значение. """

    return [operation for operation in banking_operations if operation.get("state") and operation.get('state') == state]


def sort_by_date(banking_operations: list, reverse: bool = True) -> list:
    """ Функция принимает на вход список словарей и параметр порядка сортировки,
    возвращает новый список, в котором исходные словари отсортированы по дате."""

    return sorted(banking_operations, key=lambda x: x.get('date'), reverse=reverse)
