#!/usr/bin/python3
"""
kind if class
is it?
"""

def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of,or if it is an instance of a class
    that inherited from,the specified class

    Args:
    obj: object to check
    a_class: the class to cmpare with
    Return: True if the obj is specified class ,
    otherwise False
    """
    return isinstance(obj, a_class)
