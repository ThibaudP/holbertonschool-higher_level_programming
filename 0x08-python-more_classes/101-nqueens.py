#!/usr/bin/python3
import sys
"""nqueens backtracking algorithm"""


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        exit(1)
    n = int(sys.argv[1])
    if n < 4:
        print("N must be at least 4")
        exit(1)

    # initialize the answer list (of coordinates)
    board = []
    for i in range(n):
        board.append([i, None])

    def is_safe(x, y):
        """determines if position (x, y) is safe"""

        # Check current row
        for z in range(n):
            if y == board[z][1]:
                return False

        # Check diagonals
        i = 0
        while(i < x):
            if abs(board[i][1] - y) == abs(i - x):
                return False
            i += 1
        # Position is safe!
        return True

    def solve(x):
        """solves and backtracks when encountering conflicts"""
        # loop through cols
        for y in range(n):
            # clear column
            for i in range(x, n):
                board[i][1] = None

            # checks if pos is safe (current col y + x row)
            if is_safe(x, y):
                board[x][1] = y
                # accept and print if we have the final # of queens
                if (x == n - 1):
                    print(board)
                # move to next column if not
                else:
                    solve(x + 1)

    # start the recursive process at x = 0
    solve(0)
