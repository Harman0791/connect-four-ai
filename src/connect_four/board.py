ROWS = 6
COLS = 7
EMPTY = 0

class Board:
    def __init__(self):
        self.grid = [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]
