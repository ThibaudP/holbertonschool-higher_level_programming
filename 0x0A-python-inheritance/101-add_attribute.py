#!/usr/bin/python3
"""add_attribute module"""


def add_attribute(obj, name, value):
    """Adds a new attribute to `obj` if it's possible"""
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)