#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    for y in range(x):
        try:
            print(my_list[y], end='')
            i += 1
        except:
            break
    print("\n", end='')
    return i
