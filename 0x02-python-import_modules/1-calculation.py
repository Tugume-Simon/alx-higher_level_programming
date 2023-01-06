#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    a = 10
    b = 5
    print("{:d} + {:d} = {:d}".format(a, b, add(10, 5)))
    print("{:d} - {:d} = {:d}".format(a, b, sub(10, 5)))
    print("{:d} * {:d} = {:d}".format(a, b, mul(10, 5)))
    print("{:d} / {:d} = {:d}".format(a, b, div(10, 5)))
