#!/usr/bin/python3
"""Contains The N queens puzzle Challenge """

import sys


def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at position (row, col)
    on the board.

    Args:
        board (list): The current state of the chessboard.
        row (int): The row index.
        col (int): The column index.

    Returns:
        bool: True if safe, False otherwise.
    """
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper diagonal on the right side
    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens_util(board, row):
    """
    Recursive utility function to solve the N Queens problem.

    Args:
        board (list): The current state of the chessboard.
        row (int): The current row to place the queen.

    Returns:
        None
    """
    if row == len(board):
        # Print the solution as a list of coordinates (row, col)
        solution = [[i, board[i].index(1)] for i in range(len(board))]
        print(solution)
        return

    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 1
            solve_nqueens_util(board, row + 1)
            board[row][col] = 0


def solve_nqueens(n):
    """
    Solve the N Queens problem.

    Args:
        n (str): The size of the chessboard.

    Returns:
        None
    """
    if not n.isdigit():
        print("N must be a number")
        sys.exit(1)

    n = int(n)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(n)] for _ in range(n)]
    solve_nqueens_util(board, 0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    solve_nqueens(sys.argv[1])
