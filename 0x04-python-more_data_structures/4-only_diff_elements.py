#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    set_combined = set(set_1)
    for el in set_2:
        if not el in set_1:
            set_combined.add(el)
    return set_combined
