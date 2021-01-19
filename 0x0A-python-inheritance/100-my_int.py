#!/usr/bin/python3
"""MyInt module"""


class MyInt(int):
    """MyInt class, extends int"""

    def __eq__(self, foreign):
        """Behavior when compared with =="""
        if issubclass(type(foreign), int):
            return int(self) != foreign

    def __ne__(self, foreign):
        """Behavior when compared with !="""
        if issubclass(type(foreign), int):
            return int(self) == foreign
