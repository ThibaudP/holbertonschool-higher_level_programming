#!/usr/bin/python3
import dis
MagicClass = __import__('103-magic_class').MagicClass

dis.dis(MagicClass)

my_circle = MagicClass(3)

print("Area: {}".format(my_circle.area()))
print("Circumference: {}".format(my_circle.circumference()))
