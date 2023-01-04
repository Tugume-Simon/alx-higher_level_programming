#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    lastDigit = number % 10
else:
    lastDigit = -1 * (-number % 10)
print(f"Last digit of {number} is {lastDigit} and is", end=" ")
if lastDigit > 5:
    print("greater than 5")
elif lastDigit == 0:
    print("0")
elif lastDigit < 6 and lastDigit != 0:
    print("less than 6 and not 0")

