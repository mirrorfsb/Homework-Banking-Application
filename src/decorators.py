import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def log(filename=None):
    """Декоратор, который автоматически будет логировать
    начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки."""
    def wrapper(function):
        def inner(*args, **kwargs):
            result = None  # Предварительное объявление переменной

            try:
                # Выполняем функцию и сохраняем результат
                result = function(*args, **kwargs)
                output_result = f"{function.__name__} ok"
            except Exception as e:
                # Если возникла ошибка, формируем сообщение об ошибке
                output_result = (f"{function.__name__} "
                                 f"error: {type(e).__name__}. "
                                 f"Inputs: {args}, {kwargs}")
            # Логируем результат
            if filename is None:
                print(output_result)
            else:
                with open(filename, "a") as file:
                    file.write(output_result)
                    file.write("\n")
            # Возвращаем результат функции (если не было ошибки)
            return result
        return inner
    return wrapper


@log()
def my_function(x, y):
    return x + y


my_function(1, 2)
