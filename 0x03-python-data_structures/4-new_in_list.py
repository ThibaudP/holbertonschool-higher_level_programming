#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list.copy()
    if new_list and 0 <= idx < len(my_list):
        new_list[idx] = element
        return (new_list)
    else:
        return (new_list)
