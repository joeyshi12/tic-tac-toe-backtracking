from typing import List

LINES = [[[i, j] for i in range(3)] for j in range(3)]\
    + [[[j, i] for i in range(3)] for j in range(3)]\
    + [[[i, i] for i in range(3)], [[2 - i, i] for i in range(3)]]


def optimal_decision(board: List[List[str]]) -> List[int]:
    index = None
    max_score = -float("inf")
    for i in range(3):
        for j in range(3):
            if board[i][j] != ".":
                continue
            board[i][j] = "o"
            score = get_score(board, True, 1)
            board[i][j] = "."
            if score > max_score:
                index = [i, j]
                max_score = score
    return index


def get_score(board: List[List[str]], is_player_turn: bool, level: int) -> int:
    winner = get_winner(board)
    if winner == "o":
        return 1 / level
    if winner == "x":
        return -0.5 / level
    num_solutions = 0
    for i in range(3):
        for j in range(3):
            if is_valid_choice(board, i, j):
                board[i][j] = "x" if is_player_turn else "o"
                num_solutions += get_score(board, not is_player_turn, level + 1)
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
