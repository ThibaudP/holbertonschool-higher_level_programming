#!/usr/bin/python3
"""Square module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class, extends Rectangle"""

    def __init__(self, size):
        """Constructor for Square class"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Returns the area of the Square object"""
        return (self.__size ** 2)
