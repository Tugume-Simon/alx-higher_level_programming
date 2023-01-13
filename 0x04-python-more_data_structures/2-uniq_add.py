#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    for value in set(my_list):
        sum = sum + value
    return sum
