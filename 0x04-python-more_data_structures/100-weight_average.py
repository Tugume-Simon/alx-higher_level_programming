#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == [] or my_list is None:
        return 0
    prdt = 0
    quot = 0
    for (x, y) in my_list:
        prdt += x * y
        quot += y
    return prdt / quot
