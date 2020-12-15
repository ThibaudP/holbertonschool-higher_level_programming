#!/usr/bin/python3
def max_integer(my_list=[]):
    maxn = my_list[0]
    if my_list:
        for x in my_list:
            if x > maxn:
                maxn = x
        return maxn
    else:
        return None
