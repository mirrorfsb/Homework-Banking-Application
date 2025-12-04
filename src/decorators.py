import logging
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


def setup_logger(name, log_file, level=logging.INFO, filemode='a'):
    """Универсальная функция для настройки логеров"""

    log_dir = os.path.dirname(log_file)
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    file_handler = logging.FileHandler(log_file, mode=filemode, encoding='utf-8')
    file_handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Очищаем предыдущие обработчики (чтобы избежать дублирования)
    if logger.handlers:
        logger.handlers.clear()

    # Добавляем обработчик
    logger.addHandler(file_handler)

    return logger


def logger_masks(func):
    """Декоратор для логирования функций модуля masks"""
    logger = setup_logger(
        "masks",
        "logs/masks.log",  # Относительный путь
        filemode='a'  # Добавление в конец файла вместо перезаписи
    )

    @wraps(func)
    def wrapper(args, kwargs):
        logger.info(f"Function {func.__name__} called with args: {args}, kwargs: {kwargs}")
        try:
            result = func(args, kwargs)
            logger.info(f"Function {func.__name__} returned: {result}")
            return result
        except Exception as e:
            logger.error(f"Function {func.__name__} raised exception: {e}")
            raise

    return wrapper


def logger_utils(func):
    """Декоратор для логирования функций модуля utils"""
    logger = setup_logger(
        "utils",
        "logs/utils.log",  # Относительный путь
        filemode='a'
    )

    @wraps(func)
    def wrapper(args, kwargs):
        logger.info(f"Function {func.__name__} called with args: {args}, kwargs: {kwargs}")
        try:
            result = func(args, kwargs)
            logger.info(f"Function {func.__name__} returned: {result}")
            return result
        except Exception as e:
            logger.error(f"Function {func.__name__} raised exception: {e}")
            raise

    return wrapper
