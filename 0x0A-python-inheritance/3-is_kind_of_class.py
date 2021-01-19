#!/usr/bin/python3
"""is_kind_of_class module"""


def is_kind_of_class(obj, a_class):
    """Checks if object is of the `a_class` class
    or is a subclass of `a_class`"""
    if isinstance(obj, a_class):
        return True
    return False
