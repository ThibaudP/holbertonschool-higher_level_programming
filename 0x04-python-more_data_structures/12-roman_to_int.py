#!/usr/bin/python3
def roman_to_int(roman_string):
    val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    res = 0
    for i in range(len(roman_string)):
        if i > 0 and val[roman_string[i]] > val[roman_string[i - 1]]:
            res += val[roman_string[i]] - 2 * val[roman_string[i - 1]]
        else:
            res += val[roman_string[i]]
    return res
