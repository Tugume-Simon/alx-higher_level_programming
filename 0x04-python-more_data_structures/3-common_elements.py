#!/usr/bin/python3
def common_elements(set_1, set_2):
    common = []
    for el in set_1:
        for lang in set_2:
            if lang == el:
                common.append(lang)
    return common
