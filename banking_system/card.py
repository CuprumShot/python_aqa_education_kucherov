import random


def luhn_algorithm(card):
    card = list(map(int, card))
    for counts, numbers in enumerate(card, 1):
        if counts % 2 != 0:
            card[counts - 1] *= 2
        if card[counts - 1] > 9:
            card[counts - 1] -= 9
    return sum(card)
    # card_number_sum = sum(card)
    # if card_number_sum % 10 == 0:
    #     return True
    # else:
    #     return False


def start_balance(luhn_sum):
    return 10 - luhn_sum % 10 if luhn_sum % 10 != 0 else 0


def generate_card_number(account_card_number):
    iin = "400000"
    luhn_sum = luhn_algorithm(iin + account_card_number)
    checksum = start_balance(luhn_sum)
    yield iin + account_card_number + str(checksum)


def generate_account_number():
    account_card_number = ""
    for digits in range(9):
        account_card_number += str(random.randrange(10))
    return account_card_number


def pin_code_generator():
    card_pin_code = ''
    for digits in range(4):
        card_pin_code += str(random.randrange(10))
    return card_pin_code
