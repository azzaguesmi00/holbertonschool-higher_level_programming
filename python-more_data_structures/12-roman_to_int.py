#!/usr/bin/python3
def roman_to_int(roman_string):
    ro_num = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    number = 0
    i = 0

    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    for x in roman_string[::-1]:
        valeur = ro_num[x]
        if valeur < i:
            number -= valeur
        else:
            number += valeur
        i = valeur
    return number
