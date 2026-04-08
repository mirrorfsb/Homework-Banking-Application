import logging

logger = logging.getLogger("masks")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("../logs/masks.log', encoding='utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску.
    Номер карты замаскирован и отображается в формате XXXX XX** **** XXXX"""
    logger.info("Проверяем номер карты")
    cleaned_number = "".join(filter(str.isdigit, card_number))

    if len(cleaned_number) < 16:
        logger.error("Произошла ошибка: некорректный номер")
        return "Введен некорректный номер"

    mask_card_number = f"{cleaned_number[:4]} {cleaned_number[4:6]}** **** {cleaned_number[12:]}"
    logger.info("Возвращаем маску номера")
    return mask_card_number


if __name__ == "__main__":
    print(get_mask_card_number("1234 5678 9012 3456"))


def get_mask_account(account_number: str | int) -> str:
    """Функция принимает на вход номер счета и возвращает его маску.
    Номер счета замаскирован и отображается в формате XXXX"""
    logger.info("Проверяем номер счета")

    try:
        # Преобразуем в строку и убираем пробелы
        account_str = str(account_number).replace(" ", "")

        # Проверяем, что это цифры
        if not account_str.isdigit():
            logger.error("Номер счета содержит недопустимые символы")
            return "Введен некорректный номер"

        # Проверяем длину
        if len(account_str) < 4:
            logger.error("Слишком короткий номер счета")
            return "Введен некорректный номер"

        # Возвращаем маску
        return f"**{account_str[-4:]}"

    except (TypeError, ValueError, AttributeError):
        logger.error("Некорректный тип данных для номера счета")
        return "Введен некорректный номер"


if __name__ == "__main__":
    print(get_mask_account("12345678901234567890"))
