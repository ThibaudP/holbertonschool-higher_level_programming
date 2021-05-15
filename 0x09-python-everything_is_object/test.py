#!/usr/bin/python3
a = 2048
b = 2048
print(id(a))
print(id(b))
del a
del b
c = 2048
print(id(c))