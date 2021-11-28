"""Tic Tac Toe menu"""

import logging
import sys
import time
from pathlib import Path
from game_board import Board
from player_menu import Player


Path("logs").mkdir(parents=True, exist_ok=True)
FILENAME = 'logs/tictactoe.log'


def configure_logger():
    # logger configuring
    logger = logging.getLogger(__name__)
    file_handler = logging.FileHandler(FILENAME)
    file_handler.setLevel(logging.WARNING)
    file_format = logging.Formatter('%(pastime)s %(message)s', "%d-%b-%Y %H:%M:%S")
    file_handler.setFormatter(file_format)
    logger.addHandler(file_handler)

    stream_handler = logging.StreamHandler(sys.stdout)

    stream_handler.setLevel(logging.WARNING)
    console_format = logging.Formatter('%(message)s')
    stream_handler.setFormatter(console_format)
    logger.addHandler(stream_handler)
    return logger


log = configure_logger()


def timer(func):
    # timer decorator
    def wrapper(*args_for_function):
        start = time.time()
        func(*args_for_function)
        end = time.time()
        total_time = (end - start)
        log.warning(f'Game duration time was: {total_time.__round__(2)}')
    return wrapper


class MainMenu:
    # main menu options
    def __init__(self):
        self.main_menu()

    def main_menu(self):
        # main menu
        options = {'1': 'Play game', '2': 'Show Logs', '3': 'Clear Logs', '0': 'Exit'}
        actions = {'1': self.start_game, '2': self.show_logs, '3': self.clear_logs, '0': exit}
        for i in options:
            print(f"{i}: {options.get(i)}", sep="\n")
        try:
            user_choice = input('> ')
            actions[user_choice]()
        except KeyError:
            print("This option does not exist.\nPlease try again")
        return self.main_menu()

    @staticmethod
    def start_game():
        # start the game
        player_one = Player('X')
        player_two = Player('O')
        game = TicTacToe(player_one, player_two)
        game.game_process()

    @staticmethod
    def show_logs():
        # show logs
        try:
            with open(FILENAME, "r") as log_file:
                print(log_file.read())
        except OSError:
            log.critical('File not found')
        else:
            log_file.close()

    @staticmethod
    def clear_logs():
        # logger clearing
        try:
            with open(FILENAME, "w") as log_file:
                log_file.truncate()
        except OSError:
            log.critical('File not found')
        else:
            log_file.close()


class TicTacToe:
    # game class
    def __init__(self, player_one, player_two):
        self.board = Board()
        self.player_one = player_one
        self.player_two = player_two
        self.current_player = self.player_one
        self.winner = None

    def game_process(self):
        # two stage of the game
        self.game()
        self.rematch()

    @timer
    def game(self):
        # game method
        self.board.create_board()
        while True:
            self.board.display_board()
            coordinates = self.current_player.get_coordinates()
            current_token = self.current_player.token
            if not self.board.add_token(coordinates, current_token):
                print("You can't go there!")
                self.flip_players()
            if self.check_game_over():
                break
            self.flip_players()
        if self.winner is not None:
            log.warning(f'{self.winner} wins')
        elif self.winner is None:
            log.warning(f'Draw between {self.player_one.name} and {self.player_two.name}')
        self.board.display_board()

    def rematch(self):
        # rematch stage functionality
        rematch_ask = input("Wanna play again? (Enter 'yes' or 'no'): ")
        if rematch_ask.lower() == 'yes':
            self.current_player = self.player_one
            self.board = Board()
            self.game_process()
        else:
            exit()

    def check_game_over(self):
        # check if the game is final
        if self.board.win_one_two():
            self.winner = self.current_player.name
            return True
        elif self.board.draw():
            self.winner = None
            return True

    def flip_players(self):
        # changing player's turn
        if self.current_player == self.player_one:
            self.current_player = self.player_two
        else:
            self.current_player = self.player_one


def main():
    # main method
    game = MainMenu()
    game.main_menu()


if __name__ == '__main__':
    main()
