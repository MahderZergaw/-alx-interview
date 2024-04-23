#!/usr/bin/python3
"""This module implements a Backtracking Algorithm for the n queens problem"""

import sys


def checkUsageSpecs():
    """Validates the parameters passed by the user on the command line"""
    # Usage Specifications
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        sys.exit(1)

    n = sys.argv[1]

    if not n.isdecimal():
        print('N must be a number')
        sys.exit(1)

    n = int(n)

    if n < 4:
        print('N must be at least 4')
        sys.exit(1)

    return n


def validPlacementOrNot(queensCoordinates, row, n):
    """Checks if the position of the queen is not in the line of attack
    of an already placed queen
    """
    # Check horizontal line
    horizontalLineClear = True
    for j in range(len(queensCoordinates) - 2, -1, -1):
        if queensCoordinates[j][1] == row:
            horizontalLineClear = False
            return False

    if horizontalLineClear is True:
        # Check upper diagonal line
        upperDiagonalLineClear = True
        x = row
        for j in range(len(queensCoordinates) - 2, -1, -1):
            if x >= n - 1:
                break
            if queensCoordinates[j][1] == x + 1:
                upperDiagonalLineClear = False
                return False
            x += 1

        if upperDiagonalLineClear is True:
            # Check lower diagonal line
            x = row
            for j in range(len(queensCoordinates) - 2, -1, -1):
                if x < 0:
                    break
                if queensCoordinates[j][1] == x - 1:
                    return False
                x -= 1
            return True


def solveNQueens(n, column, queensPosition, allPlacements):
    """Backtracking algorithm to find all the possible positions for
    N non-attacking queens on an N x N chessboard
    """
    if column == n:
        allPlacements.append(queensPosition.copy())
    else:
        for row in range(n):
            queensPosition.append([column, row])
            if validPlacementOrNot(queensPosition, row, n) is True:
                solveNQueens(n, column + 1, queensPosition, allPlacements)
            queensPosition.remove([column, row])


def nQueensWrapper():
    """The entry point for the nqueens algorithm"""
    n = checkUsageSpecs()
    allPlacements = []

    solveNQueens(n, 0, [], allPlacements)

    for placement in allPlacements:
        print(placement)


nQueensWrapper()
