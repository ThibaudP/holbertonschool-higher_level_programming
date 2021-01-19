#!/usr/bin/python3
"""Rectangle module"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class, extends BaseGeometry"""

    def __init__(self, width, height):
        """Constructor for Rectangle class"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns the area of the Rectangle object"""
        return (self.__width * self.__height)

    def __str__(self):
        """Sets the string behavior of the Rectangle objects"""
        return "[Rectangle] "+str(self.__width)+"/"+str(self.__height)
