#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digt = abs(number) % 10

if (number < 0):
    last_digt = -last_digt

print(f"Last digit of {number} ", end="")
if (last_digt > 5):
    print(f"is {last_digt} and is greater than 5")
elif (last_digt == 0):
    print(f"is {last_digt} and is 0")
elif (last_digt < 6 and last_digt != 0):
    print(f"is {last_digt} and is less than 6 and not 0")
