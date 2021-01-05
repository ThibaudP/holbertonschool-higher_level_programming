#!/usr/bin/python3
"""Square module.

This module contains a class that defines a square, its size,
as well as methods to draw it with and without XY position offset.

"""


class Square:
    """This class contains a square

    """
    def __init__(self, size=0):
        """__init__ method
        Args:
            size (int): size of the square
        Raises:
            TypeError: If ``size`` is not an int
            ValueError: If ``size`` is negative

        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """area method

        Returns the area of the square

        """
        return (self.__size ** 2)
