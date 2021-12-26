from card import generate_card_number
from card import generate_account_number
from card import pin_code_generator

import sqlite3
from collections import namedtuple
import time


class BankingSystem:
    Account = namedtuple('Account', 'id, card, pin, balance')
    CONNECTION = sqlite3.connect('card.s3db')
    CURSOR = CONNECTION.cursor()

    __START_MENU = {1: 'Create an account', 2: 'Log into account', 0: 'Exit'}
    __ACCOUNT_PANEL = {1: 'Balance', 2: 'Add Income', 3: 'Do Transfer',
                       4: 'Close Account', 5: 'Log Out', 0: 'Exit'}
    __WRONG_INPUT = 'This option does not exist. Please try again\n'
    __MAIN_MENU = 1
    __ACCOUNT_MENU = 2
    __ATTEMPTS = 0

    def __init__(self):
        self.sql = self.CURSOR.executescript('''CREATE TABLE IF NOT EXISTS CARD
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        number TEXT NOT NULL,
        pin_code TEXT NOT NULL,
        balance INTEGER NOT NULL DEFAULT 0)''')
        self.CONNECTION.commit()
        self.curr_card = None
        self.curr_pin = None
        self.state = self.__MAIN_MENU
        self.account = None
        self.__MAIN_ACTIONS = {1: self.new_account, 2: self.log_in, 0: self.exit}

    def start(self):
        if self.state == self.__MAIN_MENU:
            for i in self.__START_MENU:
                print(f'{i}:\n{self.__START_MENU.get(i)}')
        elif self.state == self.__ACCOUNT_MENU:
            for i in self.__ACCOUNT_PANEL:
                print(f'{i}:\n{self.__ACCOUNT_PANEL.get(i)}')
        return '> '

    def take_action(self, action):
        if self.check_user_input(action):
            return self.make_action(action)
        else:
            print(self.__WRONG_INPUT)
            return self.start()

    def make_action(self, action):
        if self.state == self.__MAIN_MENU:
            self.__MAIN_ACTIONS[action]()
        elif self.state == self.__ACCOUNT_MENU:
            if action in range(4, 6):
                self.state = self.__MAIN_MENU
            elif action == 0:
                return self.exit()
            self.account.ACCOUNT_ACTIONS[action]()

    def check_user_input(self, action):
        if self.state == self.__MAIN_MENU:
            if action in range(0, 3):
                return True
        elif self.state == self.__ACCOUNT_MENU:
            if action in range(0, 6):
                return True
        elif action == 0:
            self.exit()
        return False

    def new_account(self):
        print('Your card has been created!')
        accounts = self.get_all_accounts()
        while True:
            new_number = generate_account_number()
            card = next(generate_card_number(new_number))
            if card not in accounts.keys():
                break
        pin_code = pin_code_generator()
        print(f'\nYour card number:\n{card}\nYour card PIN:\n{pin_code}\n')
        self.CURSOR.execute(f'INSERT INTO card(number, pin_code) VALUES ({card}, {pin_code})')
        self.CONNECTION.commit()

    @staticmethod
    def get_all_accounts():
        accounts = {}
        for acc in accounts:
            accounts[acc.card] = acc.pin_code
        return accounts

    def exists_credentials(self):
        # take exist creds
        self.CURSOR.execute('SELECT * from card')
        result = self.CURSOR.fetchall()
        print(result)

    def log_in(self, card=None, pin=None, brute_force=False):
        self.exists_credentials()
        if not brute_force:
            self.credentials(self.ask_card_number(), self.ask_pin_code())
        else:
            self.credentials(card, pin)
        account = self.get_account(self.curr_card, self.curr_pin)
        if account:
            self.__ATTEMPTS = 0
            self.state = self.__ACCOUNT_MENU
            print('\nYou have successfully logged in!\n')
        else:
            self.__ATTEMPTS += 1
            if self.__ATTEMPTS >= 3:
                print('Sorry, hacking attempt detected. Please, wait until system will be unlocked')
                time.sleep(60)
            else:
                print('Wrong card number or PIN!')

    def credentials(self, card, pin):
        self.curr_card = card
        self.curr_pin = pin

    @staticmethod
    def ask_card_number():
        user_card = int(input('Enter your card number:\n> '))
        return user_card

    @staticmethod
    def ask_pin_code():
        user_pin = int(input('Enter your PIN:\n> '))
        return user_pin

    def get_account(self, account_number, pin_code):
        self.CURSOR.execute(f'SELECT * FROM card WHERE number = {account_number} AND pin_code = {pin_code}')
        account = self.CURSOR.fetchone()
        return self.Account._make(account) if account else None

    def check_attempts(self, card):
        self.CURSOR.execute(f'SELECT attempt FROM CARD WHERE NUMBER = {card}')
        attempt = self.CURSOR.fetchone()
        return attempt

    def get_attempt(self, card):
        self.CURSOR.execute(f'SELECT attempt FROM CARD WHERE NUMBER = {card}')
        attempt = self.CURSOR.fetchone()[0]
        return attempt

    def add_attempt(self, card):
        self.CURSOR.execute(f'UPDATE CARD SET attempt = attempt + 1 WHERE NUMBER = {card}')
        self.CONNECTION.commit()

    def exit(self):
        print('Bye!')
        self.CONNECTION.close()
        self.state = 'off'


def main():
    bank = BankingSystem()
    response = bank.start()
    while True:
        user_input = int(input(response))
        response = bank.take_action(user_input)
        if bank.state == 'off':
            break
        elif response is None:
            response = bank.start()


if __name__ == '__main__':
    main()
