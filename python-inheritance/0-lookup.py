#!/usr/bin/python3

def lookup(obj):
    """return a list of available attributes and methods
    for a object
    
    
    Args: 
         obj: object to inspect
    
    Returns:
         A list containing the attributes and methods 
         of the object
    """
    return dir(obj)
