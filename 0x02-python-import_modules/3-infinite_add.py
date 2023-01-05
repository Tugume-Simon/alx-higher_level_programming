#!/usr/bin/python3
from sys import argv
sum = 0
for i in range(1, len(argv)):
    sum = sum + int(argv[i])

print("{}".format(sum))
