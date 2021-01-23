#!/usr/bin/python3
"""base module"""


class Base():
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor for Base"""
        if id is None:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
        else:
            self.id = id
