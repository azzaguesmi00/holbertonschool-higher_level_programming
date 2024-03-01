#!/usr/bin/python3
"""
inherits from
"""


def inherits_from(obj, a_class):
    """
    obj: the object to track
    a_class: the class to compare
    return true if type(obj) is a_class
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
