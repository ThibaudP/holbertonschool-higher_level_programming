#!/usr/bin/python3
"""student module"""


class Student():
    """Student class"""
    def __init__(self, first_name="", last_name="", age=""):
        """constructor for Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns the dict for json serialization"""
        if attrs is not None:
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        else:
            return self.__dict__
