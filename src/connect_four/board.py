ROWS = 6
COLS = 7
EMPTY = 0
SYMBOLS = {EMPTY: ".", 1: "X", 2: "O"}

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

    def is_winner(self, player):
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        for row in range(ROWS):
            for col in range(COLS):
                for d_row, d_col in directions:
                    end_row = row + 3 * d_row
                    end_col = col + 3 * d_col
                    if not (0 <= end_row < ROWS and 0 <= end_col < COLS):
                        continue
                    if all(
                        self.grid[row + i * d_row][col + i * d_col] == player
                        for i in range(4)
                    ):
                        return True
        return False

    def is_full(self):
        return not self.valid_moves()

    def __str__(self):
        return "\n".join(
            " ".join(SYMBOLS[cell] for cell in row) for row in self.grid
        )