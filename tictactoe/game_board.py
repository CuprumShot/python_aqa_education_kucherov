"""Board functionality"""


class Board:
    # board class description
    def __init__(self):
        self.board = []

    def create_board(self):
        # board creating
        for i in range(0, 9):
            self.board.extend('-')
        return self.board

    def display_board(self):
        # displays board in terminal
        print('''
                 {} | {} | {}
                ---+---+---
                 {} | {} | {}
                ---+---+---
                 {} | {} | {}
                '''.format(*self.board))

    def add_token(self, position, token):
        # adding players token to the board 'X' or 'O'
        if self.board[position] != '-':
            return False
        else:
            self.board[position] = token
        return True

    def win_one_two(self):
        # winner checking
        combs = [[0, 3, 6], [0, 1, 2], [0, 2]]
        for j in combs[0]:
            if self.rows(self.board[j:j+3]):
                return True
        for j in combs[1]:
            if self.columns(self.board[j:j+7:3]):
                return True
        for j in combs[2]:
            if self.diagonals(self.board[j:j+9:4]):
                return True

    @staticmethod
    def rows(row):
        # rows checking
        if all([i == 'X' for i in row]) or all([i == 'O' for i in row]):
            return True

    @staticmethod
    def columns(column):
        # columns checking
        if all([i == 'X' for i in column]) or all([i == 'O' for i in column]):
            return True
        return

    @staticmethod
    def diagonals(diagonal):
        # diagonals checking
        if all([i == 'X' for i in diagonal]) or all([i == 'O' for i in diagonal]):
            return True
        return

    def draw(self):
        # check the draw result
        if '-' not in self.board:
            return True
