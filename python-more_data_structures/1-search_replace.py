#!/usr/bin/python3
def search_replace(my_list, search, replace):
    for i in my_list:
         new_list = [replace if item == search else item for item in my_list]
    
    return new_list
