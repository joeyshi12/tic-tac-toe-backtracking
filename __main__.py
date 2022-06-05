from typing import List
import random
import util


def make_decision(board: List[List[str]], is_player_turn: bool) -> List[int]:
    if not is_player_turn:
        print("AI is deciding...")
        decision = util.optimal_decision(board)
        print(f"AI chooses {decision}")
        return decision
    choice = input("Make a choice: ").split()
    if len(choice) != 2:
        return []
    if any(not val.isdigit() for val in choice):
        return []
    return map(int, choice)


def main():
    is_player_turn = random.random() > 0.5
    board = [["."] * 3 for _ in range(3)]
    while True:
        decision = make_decision(board, is_player_turn)
        if not decision:
            print("Invalid decision")
            continue

        i, j = decision
        if not util.is_valid_choice(board, i, j):
            print("Invalid choice")
            continue

        board[i][j] = "x" if is_player_turn else "o"
        util.print_board(board)

        if util.is_tied(board):
            print("Game tied")
            break

        winner = util.get_winner(board)
        if winner:
            print(f"{winner} is the winner")
            break

        is_player_turn = not is_player_turn


if __name__ == "__main__":
    main()
