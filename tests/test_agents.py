from connect_four.agents import HeuristicAgent, RandomAgent
from connect_four.board import ROWS, Board


def test_random_agent_picks_a_valid_move():
    board = Board()
    for _ in range(ROWS):
        board.drop_piece(0, 1)
    agent = RandomAgent(seed=42)
    for _ in range(50):
        assert agent.choose_move(board, 2) in board.valid_moves()


def test_random_agent_with_same_seed_repeats_its_choices():
    first = RandomAgent(seed=7)
    second = RandomAgent(seed=7)
    board = Board()
    moves_a = [first.choose_move(board, 1) for _ in range(10)]
    moves_b = [second.choose_move(board, 1) for _ in range(10)]
    assert moves_a == moves_b


def test_heuristic_takes_a_winning_move():
    board = Board()
    for _ in range(3):
        board.drop_piece(0, 1)
    assert HeuristicAgent().choose_move(board, 1) == 0


def test_heuristic_blocks_opponent():
    board = Board()
    for _ in range(3):
        board.drop_piece(6, 2)
    assert HeuristicAgent().choose_move(board, 1) == 6


def test_heuristic_prefers_winning_over_blocking():
    board = Board()
    for _ in range(3):
        board.drop_piece(0, 1)
        board.drop_piece(6, 2)
    assert HeuristicAgent().choose_move(board, 1) == 0


def test_heuristic_plays_centre_on_empty_board():
    assert HeuristicAgent().choose_move(Board(), 1) == 3