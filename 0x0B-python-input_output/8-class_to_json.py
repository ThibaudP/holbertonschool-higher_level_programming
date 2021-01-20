#!/usr/bin/python3
"""class_to_json module"""


def class_to_json(obj):
    """Returns the dict of a class"""
    return obj.__dict__
