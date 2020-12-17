#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    if set_1 and set_2:
        diff_1 = [x for x in set_1 if x not in set_2]
        diff_2 = [x for x in set_2 if x not in set_1]
        return set(diff_1 + diff_2)
