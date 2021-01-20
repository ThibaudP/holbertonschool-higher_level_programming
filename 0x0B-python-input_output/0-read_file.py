#!/usr/bin/python3
"""read_file module"""


def read_file(filename=""):
    """Prints the content of a file"""
    if type(filename) is str:
        with open(filename, "r", encoding="utf-8") as file:
            print(file.read(), end='')
