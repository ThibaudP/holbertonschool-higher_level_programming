#!/usr/bin/python3
"""pascal_triangle module"""


def pascal_triangle(n):
    """Returns the Pascal's triangle of n, as a list of lists"""
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) is not n:
        tmp = [1]
        for i in range(len(triangle[-1]) - 1):
            tmp.append(triangle[-1][i] + triangle[-1][i + 1])
        tmp.append(1)
        triangle.append(tmp)
    return triangle
