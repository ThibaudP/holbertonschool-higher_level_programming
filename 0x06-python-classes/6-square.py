#!/usr/bin/python3
"""Square module.

This module contains a class that defines a square, its size,
as well as methods to draw it with and without XY position offset.

"""


class Square:
    """This class contains a square

    Attributes:
        __size (int): size of the square
        __position (tuple): position of top left corner

    """
    def __init__(self, size=0, position=(0, 0)):
        """__init__ method

        Args:
            size (int): size of the square
            position (tuple): position of top left corner

        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """position getter

        Gets the value of private attribute __position

        Return:
            int: the size of the square

        """
        return self.__position

    @position.setter
    def position(self, value):
        """position setter

        Sets the value of private attribute __position

        Args:
            value (tuple): a tuple of coordinates

        Raises:
            TypeError: if ``value`` is not a tuple of 2 positive integers
        """
        if type(value) is tuple and len(value) == 2 and \
                type(value[0]) is int and type(value[1]) is int and \
                value[0] >= 0 and value[1] >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """area method

        Returns:
            int: the area of the square

        """
        return (self.__size ** 2)

    def my_print(self):
        """my_print method

        Prints the square starting at ``self.position``

        """
        if self.size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()

            for x in range(self.size):
                print(' ' * self.position[0], end='')
                print('#' * self.size)
