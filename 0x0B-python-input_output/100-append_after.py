#!/usr/bin/python3
"""append_after module"""


def append_after(filename="", search_string="", new_string=""):
    """Reads a file, insert new_line after search_string if it exists"""
    new = ""
    with open(filename, "r") as file:
        for line in file:
            new += line
            if search_string in line:
                new += new_string

    with open(filename, "w") as file:
        file.write(new)
