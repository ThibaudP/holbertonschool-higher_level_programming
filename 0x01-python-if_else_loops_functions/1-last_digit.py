#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    absnum = -number
else:
    absnum = number

print("Last digit of {:d} is {:d}".format(number, absnum % 10), end='')

if absnum % 10 > 5:
    print(" and is greater than 5")
elif absnum % 10 == 0:
    print(" and is 0")
elif absnum % 10 != 0 and absnum % 10 < 6:
    print(" and is less than 6 and not 0")
