from connect_four.agents import HeuristicAgent
from connect_four.board import Board, COLS


def show(board):
    print()
    print(board)
    print(" ".join(str(col + 1) for col in range(COLS)))


def ask_for_column(player):
    while True:
        text = input(f"Player {player}, choose a column (1-{COLS}): ")
        try:
            return int(text) - 1
        except ValueError:
            print("Please type a number.")


def play(opponent=None):
    board = Board()
    player = 1
    while True:
        show(board)
        if player == 2 and opponent is not None:
            col = opponent.choose_move(board, player)
            print(f"{opponent.name} plays column {col + 1}")
        else:
            col = ask_for_column(player)
        try:
            board.drop_piece(col, player)
        except ValueError:
            print(f"Column {col + 1} is full or doesn't exist. Try again.")
            continue
        if board.is_winner(player):
            show(board)
            print(f"Player {player} wins!")
            return
        if board.is_full():
            show(board)
            print("It's a draw!")
            return
        player = 3 - player


if __name__ == "__main__":
    answer = input("Play against the computer? (y/n): ").strip().lower()
    play(HeuristicAgent() if answer == "y" else None)