#!/usr/bin/python3
"""inherits_from module"""


def inherits_from(obj, a_class):
    """Checks if object from a subclass of `a_class`"""
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
