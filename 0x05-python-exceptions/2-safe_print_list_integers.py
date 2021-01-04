#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    for y in range(x):
        try:
            print("{:d}".format(my_list[y]), end='')
            i += 1
        except TypeError:
            continue
        except ValueError:
            continue
    print("")
    return i
