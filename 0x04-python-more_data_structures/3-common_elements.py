#!/usr/bin/python3
def common_elements(set_1, set_2):
    if set_1 and set_2:
        return {x for x in set_1 if x in set_2}
    # elif set_1 and not set_2:
    #     return set_1
    # elif set_2 and not set_1:
    #     return set_2
    else:
        return set()
