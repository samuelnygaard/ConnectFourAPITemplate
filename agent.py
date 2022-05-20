from math import gamma
import random
from player import PlayerAB

class Agent:
    board: None
    player_symbol: None

    def __init__(self, board, player_symbol) -> None:
        self.board = board
        self.player_symbol = player_symbol

    def get_symbol(self, i):
        return 1 if i == self.player_symbol else 0

    def transform_board(self):
        new_board = self.board
        for i in range(0, 6):
            for j in range(0, 7):
                s = self.board[i][j]
                if s == '-':
                    new_board[i][j] = None
                else:
                    new_board[i][j] = self.get_symbol(s)
        return new_board

    def next_move(self):
        board = self.transform_board()
        board_width = len(self.board[0])
        column = random.randint(0, board_width - 1)
        return column

if __name__ == '__main__':
    board = [['-', '-', '-', 'O', '-', '-', 'O'],
         ['-', 'X', '-', '-', 'O', 'O', '-'],
         ['-', 'O', '-', '-', '-', '-', '-'],
         ['O', '-', '-', 'O', 'X', '-', 'O'],
         ['-', '-', '-', '-', '-', '-', '-'],
         ['-', '-', 'O', '-', 'O', '-', '-']]
    s = 'X'

    print(Agent(board, s).next_move())
