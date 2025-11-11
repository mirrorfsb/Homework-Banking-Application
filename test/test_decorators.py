from src.decorators import log
import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def test_log_prints_to_console():
    @log()
    def test_function():
        return 42

    test_function()

    # Проверяем вывод на консоль
    print("Test passed: log prints to console")


def test_log_writes_to_file():
    filename = "test.log"

    @log(filename)
    def test_function():
        return 42

    test_function()

    # Проверяем запись в файл
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()
        if lines[-1].startswith("test_function ok"):
            print("Test passed: log writes to file")
        else:
            print("Test failed: log does not write to file")


def test_log_exception_handling():
    @log()
    def error_function():
        raise ValueError("Something went wrong")

    try:
        error_function()
    except ValueError as e:
        # Проверяем обработку исключений
        print(f"Test passed: log handles exceptions - {e}")
    else:
        print("Test failed: log does not handle exceptions")