#!/usr/bin/python3
def print_reversed_list_integer(mylist=[]):
    if mylist:
        for x in mylist[::-1]:
            print("{:d}".format(x))
