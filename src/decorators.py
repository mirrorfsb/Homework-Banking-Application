import sys
import os
from functools import wraps
from typing import Any, Callable
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

"""
from functools import wraps: Импортирует функцию wraps из модуля functools.
wraps используется для копирования метаданных
(например, имени функции) из одной функции в другую.
from typing import Callable, Any: Импортирует типы Callable и Any из модуля typing.
Callable используется для определения типа функции, а Any — для указания на любой тип данных.

"""


def log(filename: str | None = None) -> Callable:

    def _log(msg: str) -> None:
        """Объявляет вспомогательную функцию _log, которая принимает строку msg и не возвращает ничего (None).
        Эта функция отвечает за логирование сообщений.
        """
        if filename is None:
            print(msg)
        else:
            with open(filename, "a", encoding="utf-8") as file:
                file.write(msg + "\n")

    def decorator(func: Callable) -> Callable:
        """
        Декоратор @wraps(func)
        используется для обновления метаданных обернутой функции wrapper с метаданными функции func.
        """

        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            """
            Функция wrapper возвращает результат выполнения функции func.
            """
            try:
                result = func(*args, **kwargs)
            except Exception as e:
                msg = f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}"
                _log(msg)  # Передает эту строку в функцию _log для записи в журнал или обработки.
                raise
            else:
                msg = f"{func.__name__} ok"
                _log(msg)  # Передает эту строку в функцию _log для записи в журнал или обработки.
                return result

        return wrapper

    return decorator
