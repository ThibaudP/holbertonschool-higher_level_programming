#!/usr/bin/python3
"""Square module.

This module contains a class that defines a square, its size,
as well as methods to draw it with and without XY position offset.

"""


class Square:
    """This class contains a square

    Attributes:
        __size (int): size of the square

    """
    def __init__(self, size=0):
        """__init__ method
        Args:
            size (int): size of the square

        """
        self.size = size

    def area(self):
        """area method

        Returns:
            int: the area of the square

        """
        return (self.__size ** 2)

    @property
    def size(self):
        """size getter

        Gets the value of private attribute __size

        Return:
            int: the size of the square

        """
        return self.__size

    @size.setter
    def size(self, value):
        """size setter

        Sets the value of private attribute __size

        Args:
            value (int): value of the square
        Raises:
            TypeError: If ``value`` is not an int
            ValueError: If ``value`` is negative

        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def __eq__(self, foreign):
        """__eq__ method

        Sets the behavior when the object is compared with the ``==`` operator

        Args:
            foreign: foreign object to compare with ``self`` (must be a Square)

        """
        if type(foreign) is Square:
            return self.area() == foreign.area()

    def __ne__(self, foreign):
        """__ne__ method

        Sets the behavior when the object is compared with the ``!=`` operator

        Args:
            foreign: foreign object to compare with ``self`` (must be a Square)

        """
        if type(foreign) is Square:
            return self.area() != foreign.area()

    def __lt__(self, foreign):
        """__lt__ method

        Sets the behavior when the object is compared with the ``<`` operator

        Args:
            foreign: foreign object to compare with ``self`` (must be a Square)

        """
        if type(foreign) is Square:
            return self.area() < foreign.area()

    def __le__(self, foreign):
        """__le__ method

        Sets the behavior when the object is compared with the ``<=`` operator

        Args:
            foreign: foreign object to compare with ``self`` (must be a Square)

        """
        if type(foreign) is Square:
            return self.area() <= foreign.area()

    def __gt__(self, foreign):
        """__gt__ method

        Sets the behavior when the object is compared with the ``>`` operator

        Args:
            foreign: foreign object to compare with ``self`` (must be a Square)

        """
        if type(foreign) is Square:
            return self.area() > foreign.area()

    def __ge__(self, foreign):
        """__ge__ method

        Sets the behavior when the object is compared with the ``>=`` operator

        Args:
            foreign: foreign object to compare with ``self`` (must be a Square)

        """
        if type(foreign) is Square:
            return self.area() >= foreign.area()
