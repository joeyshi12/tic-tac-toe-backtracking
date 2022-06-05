from typing import List

LINES = [[[i, j] for i in range(3)] for j in range(3)]\
    + [[[j, i] for i in range(3)] for j in range(3)]\
    + [[[i, i] for i in range(3)], [[2 - i, i] for i in range(3)]]


def optimal_decision(board: List[List[str]]) -> List[int]:
    index = None
    max_possible_solutions = -float("inf")
    for i in range(3):
        for j in range(3):
            if board[i][j] != ".":
                continue
            board[i][j] = "o"
            num_solutions = possible_solutions(board, True)
            board[i][j] = "."
            if num_solutions > max_possible_solutions:
                index = [i, j]
                max_possible_solutions = num_solutions
    return index


def possible_solutions(board: List[List[str]], is_player_turn: bool) -> int:
    winner = get_winner(board)
    if winner:
        if winner == "o":
            return 1
        return -1
    num_solutions = 0
    for i in range(3):
        for j in range(3):
            if not is_valid_choice(board, i, j):
                continue
            board[i][j] = "x" if is_player_turn else "o"
            num_solutions += possible_solutions(board, not is_player_turn)
            board[i][j] = "."
    return num_solutions


def is_valid_choice(board: List[List[str]], i: int, j: int) -> bool:
    return 0 <= i <= 2 and 0 <= j <= 2 and board[i][j] == "."


def is_tied(board: List[List[str]]) -> bool:
    return all(board[i][j] != "." for i in range(3) for j in range(3))


def get_winner(board: List[List[str]]) -> str:
    for line in LINES:
        i, j = line[0]
        if board[i][j] != "." and all(board[i][j] == board[p][q] for p, q in line):
            return board[i][j]
    return ""


def print_board(board: List[List[str]]) -> None:
    horizontal_line = "-" * 13
    board_str = (
        f"\t{horizontal_line}\n"
        f"\t| {board[0][0]} | {board[0][1]} | {board[0][2]} |\n"
        f"\t{horizontal_line}\n"
        f"\t| {board[1][0]} | {board[1][1]} | {board[1][2]} |\n"
        f"\t{horizontal_line}\n"
        f"\t| {board[2][0]} | {board[2][1]} | {board[2][2]} |\n"
        f"\t{horizontal_line}"
    )
    print(board_str)
