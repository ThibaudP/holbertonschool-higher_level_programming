#!/usr/bin/python3
"""base module"""
import os
import json
import csv


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

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return str([])

        if type(list_dictionaries) is not list\
                and list_dictionaries is not None:
            raise TypeError("list_dictionaries is not a list")
        for x in list_dictionaries:
            if type(x) is not dict:
                raise TypeError("list_dictionaries is not a list of dicts")

        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """returns a dict from a json string"""
        if type(json_string) is not str and json_string is not None:
            raise TypeError("json_string must be a string")
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates instances of inherited objects from a dictionary"""
        if type(dictionary) is not dict:
            raise TypeError("dictionary must be a dict")
        if len(dictionary) == 0:
            raise ValueError("dictionary must not be empty")
        
        if cls.__name__ == "Rectangle":
            new_obj = cls(1, 1)
        else:
            new_obj = cls(1)
        new_obj.update(**dictionary)

        return new_obj

    @classmethod
    def save_to_file(cls, list_objs):
        """save current class as JSON to file"""
        if type(list_objs) is not list and list_objs is not None:
            raise TypeError("list_objs must be a list")

        list_dicts = []

        if list_objs is not None and len(list_objs) > 0:
            for x in list_objs:
                if not isinstance(x, Base):
                    raise TypeError("list_objs must be a list of instances\
                                    that inherit from Base")
                dict = x.to_dictionary()
                list_dicts.append(dict)

        with open("{:s}.json".format(cls.__name__), "w") as file:
            file.write(Base.to_json_string(list_dicts)+"\n")

    @classmethod
    def load_from_file(cls):
        """Loads a list of instances from a JSON file"""
        obj_list = []

        try:
            with open("{:s}.json".format(cls.__name__), "r") as file:
                for line in file:
                    json_list = cls.from_json_string(line)
                    for dict in json_list:
                        obj_list.append(cls.create(**dict))
                return obj_list
        except IOError:
            return obj_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save current class as CSV (comma separated) to file"""
        if type(list_objs) is not list and list_objs is not None:
            raise TypeError("list_objs must be a list")

        list_dicts = []

        if list_objs is not None or len(list_objs) > 0:
            with open("{:s}.csv".format(cls.__name__), "a") as file:
                writer = csv.writer(file)
                if cls.__name__ is "Rectangle":
                    for obj in list_objs:
                        if not isinstance(obj, Base):
                            raise TypeError("list_objs must be a list of instances\
                                            that inherit from Base")
                        writer.writerow([obj.id, obj.width, obj.height,
                                        obj.x, obj.y])
                elif cls.__name__ is "Square":
                    for obj in list_objs:
                        if not isinstance(obj, Base):
                            raise TypeError("list_objs must be a list of instances\
                                            that inherit from Base")
                        writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """Loads a list of instances from a CSV file"""
        obj_list = []

        try:
            with open("{:s}.csv".format(cls.__name__), "r") as file:
                reader = csv.reader(file)
                for args in reader:
                    if cls.__name__ is "Rectangle":
                        dict = {"id": int(args[0]),
                                "width": int(args[1]),
                                "height": int(args[2]),
                                "x": int(args[3]),
                                "y": int(args[4])}
                    elif cls.__name__ is "Square":
                        dict = {"id": int(args[0]),
                                "side": int(args[1]),
                                "x": int(args[2]),
                                "y": int(args[3])}
                    obj_list.append(cls.create(**dict))
                return obj_list
        except IOError:
            return obj_list
