#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sort = sorted(a_dictionary.items())
    for item in sort:
        print("{:s}: {}".format(item[0], item[1]))
