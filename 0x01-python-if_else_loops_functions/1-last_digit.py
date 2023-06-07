#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
res = abs(number) % 10
if number < 0:
    res = res * - 1
if res > 5:
    print(f"Last digit of {number:d} is {res:d} and is greater than 5")
elif res == 0:
    print(f"Last digit of {number:d} is {res:d} and is 0")
else:
    print(f"Last digit of {number:d} is {res:d} and is less than 6 and not 0")
