#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as err:
        sys.stderr.write("Exception: {}".format(err))
        sys.stderr.write("\n")
        return None
