def get_mask_card_number(card_number: str) -> str:
    """ Функция принимает на вход номер карты и возвращает ее маску.
    Номер карты замаскирован и отображается в формате
     XXXX XX** **** XXXX"""

    card_number = str(card_number)

    if len(card_number) == 16:
        mask_card_number = (
            f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"
        )

        return mask_card_number

    return "Введен некорректный номер"


if __name__ == "__main__":
    print(get_mask_card_number("1234567891234567"))


def get_mask_account(account_number):
    """Принимает номер счёта и возвращает его маску в формате **XXXX.
    Если вход некорректен, возвращает соответствующее сообщение."""
    if not isinstance(account_number, (str, int)):
        return "Введен некорректный номер"

    account_number_str = str(account_number)
    if len(account_number_str) >= 4:
        return f"**{account_number_str[-4:]}"
    else:
        return "Введен некорректный номер"
