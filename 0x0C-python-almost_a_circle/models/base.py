#!/usr/bin/python3
"""base module"""
import json
import os
from os import path


class Base():
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor for Base"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """turns dict to json string"""

        if type(list_dictionaries) is not list:
            raise TypeError("list_dictionaries is not a list")
        for x in list_dictionaries:
            if type(x) is not dict:
                raise TypeError("list_dictionaries is not a list of dicts")

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return str([])

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save current class as JSON to file"""
        if type(list_objs) is not list and list_objs is not None:
            raise TypeError("list_objs must be a list")

        list_dicts = []

        if list_objs is not None or len(list_objs) > 0:
            for x in list_objs:
                if not isinstance(x, Base):
                    raise TypeError("list_objs must be a list of instances\
                                    that inherit from Base")
                dict = x.to_dictionary()
                list_dicts.append(dict)

        with open("{:s}.json".format(cls.__name__), "a") as file:
            file.write(Base.to_json_string(list_dicts)+"\n")
