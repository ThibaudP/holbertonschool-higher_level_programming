#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

argc = len(sys.argv)

if argc != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)

a = int(sys.argv[1])
op = sys.argv[2]
b = int(sys.argv[3])

if op is "+":
    res = add(a, b)
elif op is "-":
    res = sub(a, b)
elif op is "*":
    res = mul(a, b)
elif op is "/":
    res = div(a, b)
else:
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)

print("{} {} {} = {}".format(a, op, b, res))
