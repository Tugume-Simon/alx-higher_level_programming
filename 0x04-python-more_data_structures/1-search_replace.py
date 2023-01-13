#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    while new_list.count(search) > 0:
        idx = new_list.index(search)
        new_list[idx] = replace
    return new_list
    
