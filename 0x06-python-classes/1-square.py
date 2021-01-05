#!/usr/bin/python3
"""Square module.

This module contains a class that defines a square, its size,
as well as methods to draw it with and without XY position offset.

"""

class Square:
    """This class contains a square

    """
    def __init__(self, size):
        """__init__ method
        Args:
            size (int): size of the square

        """
        self.__size = size
