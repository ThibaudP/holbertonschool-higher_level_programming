#!/usr/bin/python3
"""append_write module"""


def append_write(filename="", text=""):
    """Appends text to file"""
    with open(filename, "a") as file:
        return file.write(text)
