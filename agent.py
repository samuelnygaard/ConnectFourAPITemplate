import time
from math import gamma
from player import PlayerAB, PlayerMM
from board import Board

class Agent:
    board: None
    player_symbol: None
    depth = 5

    def __init__(self, board, player_symbol, depth = 5) -> None:
        self.board = board
        self.player_symbol = player_symbol
        self.depth = depth

    def get_symbol(self, i):
        return 1 if i == self.player_symbol else 0

    def transform_board(self):
        new_board = [[] for _ in range(6)]
        for j in range(0, 7):
            for i in range(0, 6):
                s = self.board[i][j]
                if s != '-':
                    new_board[i].append(self.get_symbol(s))
        return new_board

    def next_move(self, ab = True):
        board = Board()
        board.board = self.transform_board()
        isPlayerOne = self.player_symbol == 'X'
        player = PlayerAB(self.depth, isPlayerOne) if ab else PlayerMM(self.depth, isPlayerOne)
        return player.findMove(board)

if __name__ == '__main__':
    board = [['-', '-', '-', 'O', '-', '-', 'O'],
         ['-', 'X', '-', '-', 'O', 'O', '-'],
         ['-', 'O', '-', '-', '-', '-', '-'],
         ['O', '-', '-', 'O', 'X', '-', 'O'],
         ['-', '-', '-', '-', '-', '-', '-'],
         ['-', '-', 'O', '-', 'O', '-', '-']]
    s = 'X'

    start = time.time()
    print(Agent(board, s, 7).next_move())
    end = time.time()
    print('time: ')
    print(end - start)

