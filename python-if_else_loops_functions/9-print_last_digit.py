#!/usr/bin/python3
def print_last_digit(number):
    if abs(number) > 9:
        lasdig = abs(number) % 10
    elif 0 <= abs(number) <= 9:
        lasdig = abs(number)
    print(lasdig, end="")
    return lasdig            