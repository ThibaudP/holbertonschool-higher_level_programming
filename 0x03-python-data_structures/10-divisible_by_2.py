#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = [not x%2 for x in my_list]
    return (new_list)
