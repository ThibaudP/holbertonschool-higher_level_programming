#!/usr/bin/python3
"""LockedClass module"""


class LockedClass:
    """Class that locks out every attribute declaration
    that is not 'first_name'"""
    __slots__ = ['first_name']
