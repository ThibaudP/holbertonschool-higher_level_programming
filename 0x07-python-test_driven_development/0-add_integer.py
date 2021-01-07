#!/usr/bin/python3
"""add_integer module"""


def add_integer(a, b=98):
    """Takes 2 ints or floats, casts them to ints,
    adds them together and returns the result
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
