"""Player menu functionality"""


class Player:
    # all info about players
    name = None
    token = None

    def __init__(self, token):
        self.name = self.names_input()
        self.token = token

    def names_input(self):
        # function for the ask name
        self.name = input('Please, enter your name: ')
        return self.name

    def get_coordinates(self):
        # initialisation where player token will be placed
        coordinates = input(f'{self.name}, enter your coordinates: \n')
        if coordinates not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            print("Invalid input. Choose a position from 1-9: ")
            coordinates = input(f'{self.name}, enter your coordinates: \n')
        coordinates = int(coordinates) - 1
        return coordinates
