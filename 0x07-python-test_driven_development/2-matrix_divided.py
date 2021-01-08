#!/usr/bin/python3
"""Matrix divided module"""


def matrix_divided(matrix, div):
    """Divides every element of a matrix by ``div``

    """
    mtrx_typeerr = "matrix must be a matrix (list of lists) of integers/floats"

    # Check if matrix doesn't exist or isn't a list
    if not matrix or type(matrix) is not list:
        raise TypeError(mtrx_typeerr)

    # For each element in matrix, check if element is not a list
    stored = 0
    for x in matrix:
        if type(x) is not list:
            raise TypeError(mtrx_typeerr)

        # Check if all rows are the same size
        if stored == 0:
            stored = len(x)
        elif len(x) != stored:
            raise TypeError("Each row of the matrix must have the same size")

        # Check if all values in a row are float or int
        for y in x:
            if type(y) not in [float, int]:
                raise TypeError(mtrx_typeerr)

    # Check if div is not a float or an int, or if div is None
    if type(div) not in [float, int] or div is None:
        raise TypeError("div must be a number")

    # Check if div == 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(i / div, 2) for i in j] for j in matrix]
