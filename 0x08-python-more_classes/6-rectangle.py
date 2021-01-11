#!/usr/bin/python3
"""Rectangle module.

This module contains a class that defines a rectangle, its size,
as well as methods to draw it with and without XY position offset.

"""


class Rectangle:
    """This class contains a rectangle

    Attributes:
        __width (int): width of the rectangle
        __height (int): height of the rectangle
        number_of_instances (int): number of instances
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """__init__ method
        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    def __str__(self):
        """__str__ method

        Sets the string behavior when printing a Rectangle object
        """
        output = ""

        if self.width == 0 or self.height == 0:
            output += '\n'
        else:
            for x in range(self.height):
                output += '#' * self.width + '\n'

        return output[:-1]

    def __repr__(self):
        """__repr__ method

        Sets the string representation when calling a Rectangle object
        """
        return "Rectangle("+str(self.width)+", "+str(self.height)+")"

    @property
    def width(self):
        """returns the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width of the rectangle

        Args:
            value (int): new width of the rectangle
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """returns the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height of the rectangle

        Args:
            value (int): new height of the rectangle
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of the rectangle

        Returns:
            int: the area of the rectangle
        """
        return (self.width * self.height)

    def perimeter(self):
        """returns the perimeter of the rectangle

        Returns:
            int: the perimeter of the rectangle
        """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return ((2 * self.width) + (2 * self.height))

    def __del__(self):
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
