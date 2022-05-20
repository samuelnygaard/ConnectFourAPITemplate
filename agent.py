from math import gamma
import random

class Agent:
    board: List[List[str]]
    player_symbol: str

    def __init__(self, game) -> None:
        self.board = game.board
        self.player_symbol = game.player_symbol

    def next_move(self):
        board_width = len(self.board[0])
        column = random.randint(0, board_width - 1)
        return column
