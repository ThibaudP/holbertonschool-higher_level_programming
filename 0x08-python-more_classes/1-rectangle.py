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
    """

    def __init__(self, width=0, height=0):
        """__init__ method
        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.width = width
        self.height = height

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
