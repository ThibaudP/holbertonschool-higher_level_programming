#!/usr/bin/python3
"""is_same_class module"""


def is_same_class(obj, a_class):
    """Checks if object is of the `a_class` class"""
    if type(obj) is a_class:
        return True
    return False
