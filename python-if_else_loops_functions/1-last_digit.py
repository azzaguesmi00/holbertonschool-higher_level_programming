#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last_dgt = number % -10
else:
    last_dgt = number % 10
if last_dgt == 0:
    print(f'Last digit of {number} is {last_dgt} and is 0')
if last_dgt < 6:
    print(f'Last digit of {number} is {last_dgt} and is less than 6 and not 0')
else:
    print(f'Last digit of {number} is {last_dgt} and is greater than 5')
