import random

from connect_four.board import COLS

CENTRE_FIRST = sorted(range(COLS), key=lambda col: abs(col - COLS // 2))


class RandomAgent:
    name = "Random"

    def __init__(self, seed=None):
        self.rng = random.Random(seed)

    def choose_move(self, board, player):
        return self.rng.choice(board.valid_moves())


class HeuristicAgent:
    name = "Heuristic"

    def choose_move(self, board, player):
        opponent = 3 - player
        moves = board.valid_moves()
        for col in moves:
            if self._wins(board, col, player):
                return col
        for col in moves:
            if self._wins(board, col, opponent):
                return col
        for col in CENTRE_FIRST:
            if col in moves:
                return col

    @staticmethod
    def _wins(board, col, player):
        test_board = board.copy()
        test_board.drop_piece(col, player)
        return test_board.is_winner(player)