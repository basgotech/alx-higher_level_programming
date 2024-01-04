#!/usr/bin/python3
import sys

""" a program that solves the N queens problem. """

def is_safe(board, row, col, N):
    """
    Check if placing a queen at the given position is safe.

    Parameters:
        board (list): The current state of the chessboard.
        row (int): The row to check.
        col (int): The column to check.
        N (int): The size of the chessboard.

    Returns:
        bool: True if it is safe, False otherwise.
    """
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
            return False
    return True

def print_solution(board, N):
    """
    Print the current solution of the N queens problem.

    Parameters:
        board (list): The current state of the chessboard.
        N (int): The size of the chessboard.
    """
    for row in range(N):
        line = ""
        for col in range(N):
            if col == board[row]:
                line += "Q"
            else:
                line += "."
        print(line)
    print()

def solve_nqueens(board, row, N):
    """
    Recursively solve the N queens problem using backtracking.

    Parameters:
        board (list): The current state of the chessboard.
        row (int): The current row to consider.
        N (int): The size of the chessboard.
    """
    if row == N:
        print_solution(board, N)
        return
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row] = col
            solve_nqueens(board, row + 1, N)

def nqueens(N):
    """
    Solve the N queens problem for a given board size.

    Parameters:
        N (str): The size of the chessboard.

    Raises:
        ValueError: If N is not a positive integer.
    """
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)

    N = int(N)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * N
    solve_nqueens(board, 0, N)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    nqueens(sys.argv[1])
