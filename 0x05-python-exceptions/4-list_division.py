#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    div_list = []
    for i in range(list_length):
        try:
            value = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            value = 0
            print("division by 0")
        except TypeError:
            value = 0
            print("wrong type")
        except IndexError:
            value = 0
            print("out of range")
        finally:
            div_list.append(value)
    return div_list
