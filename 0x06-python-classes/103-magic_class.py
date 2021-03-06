#!/usr/bin/python3
"""MagicClass module.

This module contains a magic class that uses the real magic... of maths.
The class defines a circle by its radius, and computes the area and perimeter.
Yes, that's it. Underwhelming, right?

"""


import math


class MagicClass:
    """ This class is magic (it also defines a circle of radius self.__radius)

        Attributes:
            __radius (int): the radius of the circle

    """

    def __init__(self, radius=0):
        """Initializes the instance and sets its radius

        Args:
            radius (int): radius of the circle

        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Computes the area of the circle

        Returns a the area of the circle of radius ``self.__radius``

        """
        return ((self.__radius ** 2) * math.pi)

    def circumference(self):
        """Computes the circumference of the circle

        Returns the circumference of the circle of radius ``self.__radius``

        """
        return ((2 * math.pi * self.__radius))
