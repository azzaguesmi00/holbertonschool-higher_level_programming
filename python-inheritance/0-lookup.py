#!/usr/bin/python3

"""
    Inheritance: module file
"""

def lookup(obj):
    """
    lookup: a function that returns a list
    containing available attributes and methods
    of an object Args: 
    obj: object to inspect
    
    Returns:
    A list containing the attributes and methods 
    of the object
    
    """
    return dir(obj)
