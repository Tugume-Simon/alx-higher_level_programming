#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    argc = len(argv) - 1
    print("{} argument".format(argc), end="")
    if argc != 1:
        print("s", end="")
    if argc == 0:
        print(".")
    else:
        print(":")
        for i in range(1, len(argv)):
            print("{}: {}".format(i, argv[i]))
