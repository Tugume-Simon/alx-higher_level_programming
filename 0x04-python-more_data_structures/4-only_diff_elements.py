#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    set_combined = set(set_1)
    for el in set_2:
        if el not in set_1:
            set_combined.add(el)
        else:
            set_combined.remove(el)
    return set_combined
