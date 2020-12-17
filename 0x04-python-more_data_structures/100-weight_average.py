#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        # return sum(a * b for a, b in my_list) / sum(b for a, b in my_list)
        dico = dict(my_list)
        return sum(k * v for k, v in dico.items()) / sum(dico.values())
    else:
        return 0
