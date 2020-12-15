#!/usr/bin/python3
def element_at(my_list, idx):
    if my_list and 0 <= idx < len(my_list):
        return (my_list[idx])
    else:
        return (None)
