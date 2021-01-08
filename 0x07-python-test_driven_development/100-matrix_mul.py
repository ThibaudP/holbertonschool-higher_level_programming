#!/usr/bin/python3
"""matrix_mul module"""


def matrix_mul(m_a, m_b):
    """Multiplication of 2 matrices"""

    # Check if matrices are lists
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    # Check if matrices are lists of lists
    for x in m_a:
        if type(x) is not list:
            raise TypeError("m_a must be a list of lists")
    for x in m_b:
        if type(x) is not list:
            raise TypeError("m_b must be a list of lists")

    # Check if matrices are not empty
    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    for x in m_a:
        if len(x) == 0:
            raise ValueError("m_a can't be empty")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    for x in m_b:
        if len(x) == 0:
            raise ValueError("m_b can't be empty")

    # Check if matrices contain only integers
    for x in m_a:
        for y in x:
            if type(y) not in [int, float]:
                raise TypeError("m_a should contain only integers or floats")
    for x in m_b:
        for y in x:
            if type(y) not in [int, float]:
                raise TypeError("m_b should contain only integers or floats")

    # Check if rows have same size
    len1 = None
    for x in m_a:
        if len1 is None:
            len1 = len(x)
        if len1 != len(x):
            raise TypeError("each row of m_a must be of the same size")

    len2 = None
    for x in m_b:
        if len2 is None:
            len2 = len(x)
        if len2 != len(x):
            raise TypeError("each row of m_b must be of the same size")

    # Check if matrices can be multiplied
    if len1 != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Finally, compute the multiplication
    return [
        [sum(x * y for x, y in zip(ma_row, mb_col)) for mb_col in zip(*m_b)]
        for ma_row in m_a
    ]
