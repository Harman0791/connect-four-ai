from connect_four.board import Board, ROWS, COLS, EMPTY
import pytest

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

def test_piece_lands_at_bottom():
    board = Board()
    row = board.drop_piece(3, 1)
    assert row == ROWS - 1
    assert board.grid[ROWS - 1][3] == 1


def test_pieces_stack_on_top_of_each_other():
    board = Board()
    board.drop_piece(3, 1)
    row = board.drop_piece(3, 2)
    assert row == ROWS - 2
    assert board.grid[ROWS - 2][3] == 2


def test_dropping_into_full_column_raises_error():
    board = Board()
    for _ in range(ROWS):
        board.drop_piece(0, 1)
    with pytest.raises(ValueError):
        board.drop_piece(0, 1)


def test_dropping_outside_board_raises_error():
    board = Board()
    with pytest.raises(ValueError):
        board.drop_piece(COLS, 1)
    with pytest.raises(ValueError):
        board.drop_piece(-1, 1)


def test_valid_moves_excludes_full_columns():
    board = Board()
    assert board.valid_moves() == list(range(COLS))
    for _ in range(ROWS):
        board.drop_piece(2, 1)
    assert 2 not in board.valid_moves()