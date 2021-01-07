#!/usr/bin/python3
"""text_indentation module"""


def text_indentation(text):
    """Adds 2 new lines after ".", "?" and ":"

    """

    if type(text) is not str:
        raise TypeError("text must be a string")
    nl = 1
    for x in text:
        if x in ['.', '?', ':']:
            print(x + "\n\n", end='')
            nl = 1
        elif x == " " and nl == 1:
            print("", end='')
        else:                
            print(x, end='')
            if x == "\n":
                nl = 1
            else:
                nl = 0
