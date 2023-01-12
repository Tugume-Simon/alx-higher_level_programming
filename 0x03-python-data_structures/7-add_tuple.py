#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    la = len(tuple_a)
    lb = len(tuple_b)
    max_l = la if la > lb else lb
    new_t = ()

    if la == 0:
        tuple_a = (0,)
        la = 1
    if lb == 0:
        tuple_b = (0,)
        lb = 1
    if la > lb:
        for j in range((max_l - lb), max_l):
            tuple_b += (0,)
    elif lb > la:
        for j in range((max_l - la), max_l):
            tuple_a += (0,)

    for i in range(max_l):
        new_t += (tuple_a[i] + tuple_b[i],)

    return (new_t)
