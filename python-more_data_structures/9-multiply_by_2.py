#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = dict()
    for key, value in a_dictionary.items():
        n = value * 2
        new_dictionary.update({str(key): n})
    return new_dictionary
