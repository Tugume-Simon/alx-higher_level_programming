#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return None
    max = 0
    for item in a_dictionary.items():
        if item[1] > max:
            max = item[1]
            value = item[0]
    return value
