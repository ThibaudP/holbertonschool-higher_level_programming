#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError as err:
        sys.stderr.write("Exception: {}".format(err))
        sys.stderr.write("\n")
        return False
