#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    int_count = 0
    i = 0
    while i < x:
        try:
            print("{:d}".format(my_list[i]), end="")
        except (ValueError, TypeError):
            pass
        else:
            int_count += 1
        finally:
            i = i + 1
    print("")
    return int_count
