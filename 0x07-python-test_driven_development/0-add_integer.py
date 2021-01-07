#!/usr/bin/python3
"""Add Integer module"""
def add_integer(a, b=98):
    """Adds 2 integers (or floats) together and returns the result
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
