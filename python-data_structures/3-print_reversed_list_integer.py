#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    curs_list = my_list[::-1]
    for elf in curs_list:
      print("{:d}".format(elf))
