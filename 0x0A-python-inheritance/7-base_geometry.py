#!/usr/bin/python3
"""BaseGeometry module"""


class BaseGeometry():
    """BaseGeometry class"""
    def area(self):
        """Returns the area of the current object"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Raises an error if value is not an integer"""
        if type(value) is not int:
            raise TypeError(name+" must be an integer")
        if value <= 0:
            raise ValueError(name+" must be greater than 0")
