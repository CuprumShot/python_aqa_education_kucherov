import sqlite3


class Accounts(BaseException):
    CONNECTION = sqlite3.connect('card.s3db')
    CURSOR = CONNECTION.cursor()

    def __init__(self, data):
        self.id = data.id
        self.card = data.card
        self.pin = data.pin
        self.balance = data.balance

        self.ACCOUNT_ACTIONS = {1: self.show_balance, 2: self.add_income,
                                3: self.do_transfer, 4: self.close_account,
                                5: self.log_out, 0: self.exit}

    def show_balance(self):
        print('Balance:', self.balance)

    def add_income(self):
        try:
            income_amount = int(input('Enter income:\n> '))
            self.balance += income_amount
            self.CURSOR.execute(f'UPDATE CARD SET balance = {self.balance} WHERE id = {self.id}')
            self.CONNECTION.commit()
            print('Income was added!')
        except TypeError:
            print('It\'s not a digit value.')

    def do_transfer(self):
        card = input('Transfer\nEnter card number:\n> ')
        amount = input('Enter how much money you want to transfer:\n> ')
        if self.check_valid(card, amount):
            amount = int(amount)
            self.balance -= amount
            self.CURSOR.execute(f'UPDATE CARD SET balance = {self.balance} WHERE id = {self.id}')
            self.CURSOR.execute(f'UPDATE CARD SET balance = balance + ({amount}) WHERE number = {card}')
            self.CONNECTION.commit()
            print("Success!")

    def check_valid(self, card, amount):
        if self.check_valid_card(card):
            if self.check_valid_amount(amount):
                return True

    def check_valid_card(self, card):
        if len(card) != 16 or card.isdigit() is False:
            print("Probably you made mistake in the card number. Please try again!")
        elif card == self.card:
            print("You can't transfer money to the same account!")
        else:
            return True

    def check_valid_amount(self, amount):
        if amount.isdigit() is False or int(amount) < 0:
            print("\nIncorrect amount!")
        elif int(amount) > self.balance:
            print("\nNot enough money!")
        else:
            return True

    def get_account_id(self, card):
        self.CURSOR.execute(f'SELECT id FROM CARD WHERE NUMBER = {card}')
        account_id = self.CURSOR.fetchone()
        return account_id

    def close_account(self):
        self.CURSOR.execute(f'DELETE FROM CARD WHERE id = {self.id}')
        print('The account has been closed!')
        self.CONNECTION.commit()

    @staticmethod
    def log_out():
        print('You have successfully logged out!')

    def exit(self):
        pass
