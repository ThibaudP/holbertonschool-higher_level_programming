#!/usr/bin/python3
"""read_file module"""


def write_file(filename="", text=""):
    """Writes the value of text to a file filename"""
    with open(filename, "w") as file:
        return file.write(text)
