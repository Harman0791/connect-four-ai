from connect_four.board import Board, ROWS, COLS, EMPTY

def test_new_board_has_correct_size():
    board = Board()
    assert len(board.grid) == ROWS
    assert all(len(row) == COLS for row in board.grid)

def test_new_board_is_empty():
    board = Board()
    assert all(cell == EMPTY for row in board.grid for cell in row)


def test_rows_are_independent():
    board = Board()
    board.grid[0][0] = 1
    assert board.grid[1][0] == EMPTY