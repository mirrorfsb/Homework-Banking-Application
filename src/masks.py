from src.decorators import logger_masks


@logger_masks
def get_mask_card_number(card_number):
    masked_number = card_number[:4] + " " + card_number[4:6] + "**" + " **** " + card_number[-4:]
    return masked_number


@logger_masks
def get_mask_account(account_number):
    visible_digits = 4
    masked_number = "**" + account_number[-visible_digits:]
    return masked_number
