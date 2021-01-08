#!/usr/bin/python3
"""add_integer module

This module adds two ints or floats together and returns an int

"""


def add_integer(a, b=98):
    """Adds 2 numbers together

    """

    if type(a) in [float, int]:
        try:
            a = int(a)
        except:
            raise TypeError("a must be an integer")
    else:
        raise TypeError("a must be an integer")

    if type(b) in [float, int]:
        try:
            b = int(b)
        except:
            raise TypeError("b must be an integer")
    else:
        raise TypeError("b must be an integer")

    return (a + b)
