#!/usr/bin/python3
list_lower = list(range(98, 123, 2))
list_upper = list(range(65, 90, 2))
list_lower.reverse()
list_upper.reverse()
tuple_alpha = [[list_lower[i], list_upper[i]] for i in range(len(list_lower))]
list_alpha = sum(tuple_alpha, [])
for i in list_alpha:
    print("{:c}".format(i), end="")
