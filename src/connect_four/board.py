ROWS = 6
COLS = 7
EMPTY = 0

class Board:
    def __init__(self):
        self.grid = [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]

    def drop_piece(self, col, player):
        if not 0 <= col < COLS:
            raise ValueError(f"Column {col} is outside the board")
        for row in range(ROWS - 1, -1, -1):
            if self.grid[row][col] == EMPTY:
                self.grid[row][col] = player
                return row
        raise ValueError(f"Column {col} is full")

    def valid_moves(self):
        return [col for col in range(COLS) if self.grid[0][col] == EMPTY]