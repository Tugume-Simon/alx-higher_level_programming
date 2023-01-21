#!/usr/bin/python3
import sys
from calculator_1 import div, mul, sub, add

if __name__ == "__main__":
    if (len(sys.argv) < 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    arg1 = int(sys.argv[1])
    arg2 = int(sys.argv[3])
    operator = sys.argv[2]
    result = 0

    if operator == "+":
        result = add(arg1, arg2)
    elif operator == "-":
        result = sub(arg1, arg2)
    elif operator == "*":
        result = mul(arg1, arg2)
    elif operator == "/":
        result = div(arg1, arg2)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    print("{} {} {} = {}".format(arg1, operator, arg2, result))
