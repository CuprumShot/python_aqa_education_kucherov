"""
Coffee machine task, final
"""


def actions():
    # asking what does the customer wants
    actions_dict = {'buy': 'buy', 'fill': 'fill', 'take': 'take', 'exit': 'exit', 'remaining': 'remaining'}
    action_list = ', '.join(actions_dict.values())
    while True:
        request = input(f'Write action ({action_list}): ')
        return request


def fill_value(filling):
    return int(input(filling))


class CoffeeTime:
    # classifying the coffee types
    coffee_types = {'espresso': {'money': 4, 'water': 250, 'milk': 0, 'beans': 16, 'cups': 1},
                    'latte': {'money': 7, 'water': 350, 'milk': 75, 'beans': 20, 'cups': 1},
                    'cappuccino': {'money': 6, 'water': 200, 'milk': 100, 'beans': 12, 'cups': 1}}

    def __init__(self, money=0, water=0, milk=0, beans=0, cups=0):
        self.money = money
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups

    def bin_values(self):
        # returning what is and how many the coffee machine bin has
        return f'''The coffee machine has:
{self.water} of water
{self.milk} of milk
{self.beans} of coffee beans
{self.cups} of disposable cups
{self.money} of money
                '''

    def bin_check(self, coffee_type):
        # returning apologies when ingredients are not enough or taking away used
        if self.__dict__.get('water') <= coffee_type.get('water', 0):
            print('Sorry, not enough water!')
        elif self.__dict__.get('milk') <= coffee_type.get('milk', 0):
            print('Sorry, not enough milk!')
        elif self.__dict__.get('beans') <= coffee_type.get('beans', 0):
            print('Sorry, not enough coffee beans!')
        elif self.__dict__.get('cups') <= coffee_type.get('cups', 0):
            print('Sorry, not enough disposable cups!')
        else:
            for used_value in self.__dict__.keys():
                if self.__dict__[f'{used_value}'] == self.__dict__['money']:
                    self.__dict__[f'{used_value}'] += coffee_type.get(f'{used_value}', 0)
                else:
                    self.__dict__[f'{used_value}'] -= coffee_type.get(f'{used_value}', 0)
            return True

    def buy_menu(self):
        # selecting coffee type or returning to the main menu
        coffee_type = input('What do you want to buy? 1 - espresso, 2 - latte, '
                            '3 - cappuccino, back – to main menu: ')
        if coffee_type == 'back':
            return
        elif coffee_type == '1':
            if self.bin_check(self.coffee_types.get('espresso')):
                print('I have enough resources, making you an espresso!')
        elif coffee_type == '2':
            if self.bin_check(self.coffee_types.get('latte')):
                print('I have enough resources, making you a latte!')
        elif coffee_type == '3':
            if self.bin_check(self.coffee_types.get('cappuccino')):
                print('I have enough resources, making you a cappuccino!')
        else:
            print('\n"A robot may not harm a human being, unless he finds a way to prove that\nin the final analysis,'
                  ' the harm done would benefit humanity in general."\n')

    def fill_menu(self):
        # filling the coffee machine bin
        self.water += fill_value('Write how many ml of water you want to add: ')
        self.milk += fill_value('Write how many ml of milk you want to add: ')
        self.beans += fill_value('Write how many grams of coffee beans you want to add: ')
        self.cups += fill_value('Write how many disposable coffee cups you want to add: ')

    def take_menu(self):
        # taking money from the coffee machine bin
        if self.money > 0:
            print(f'I gave you {self.money}')
        else:
            print('The money bin is empty.')

    def select_action(self):
        # selecting the main menu action
        while True:
            action = actions()
            if action == 'exit':
                print('Thank you! Come again!')
                quit()
            elif action == 'buy':
                self.buy_menu()
            elif action == 'fill':
                self.fill_menu()
            elif action == 'take':
                self.take_menu()
            elif action == 'remaining':
                print(self.bin_values())
            else:
                print('\nWrong action! =(\n')
            return self.select_action()


def coffee_machine_proceed():
    # inputting the started value for the coffee machine and triggering the selecting action
    coffee_machine = CoffeeTime(550, 400, 540, 120, 9)
    coffee_machine.select_action()


if __name__ == '__main__':
    coffee_machine_proceed()
