#!/usr/bin/python3
class Square:
    """This class contains a square

    Attributes:
        __size (int): size of the square

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
