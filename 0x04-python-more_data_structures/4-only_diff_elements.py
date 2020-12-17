#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    if set_1 and set_2:
        return set_1.symmetric_difference(set_2)
    elif set_1 and not set_2:
        return set_1
    elif set_2 and not set_1:
        return set_2
    else:
        return set()
