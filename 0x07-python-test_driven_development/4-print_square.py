#!/usr/bin/python3
"""print_square module"""


def print_square(size):
    """Prints a square of size ``size``

    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    
    for x in range(size):
        print("#" * size)
