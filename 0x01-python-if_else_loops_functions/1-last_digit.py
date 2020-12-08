#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    rem = -((-number) % 10)
else:
    rem = number % 10

print("Last digit of {} is {} and is".format(number, rem), end=' ')

if rem > 5:
    print("greater than 5")
elif rem == 0:
    print("0")
elif rem < 6 and rem != 0:
    print("greater than 6 and not 0")
