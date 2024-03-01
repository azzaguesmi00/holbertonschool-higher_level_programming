#!/usr/bin/python3
"""
    same_class 
    is it?
"""

def is_same_class(obj, a_class):
    """ Check if object is exactly an instance of specified class

        obj: the object to check
        a_class: the class to compare with
        return true if type(obj) is a_class
    """
    return type(obj) is a_class
