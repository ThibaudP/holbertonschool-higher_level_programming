#!/usr/bin/python3
"""my_list module"""


class MyList(list):
    """MyList class, extends the built-in `list` class"""

    def print_sorted(self):
        """Prints the sorted list"""
        print(sorted(self))
