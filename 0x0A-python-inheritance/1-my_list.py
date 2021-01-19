#!/usr/bin/python3
"""my_list

    MyList object"""

class MyList(list):
    """MyList class, extends the built-in list class

    """

    def print_sorted(self):
        """Prints the sorted list"""
        sortedlist = self.copy()
        sortedlist.sort()
        print(sortedlist)
