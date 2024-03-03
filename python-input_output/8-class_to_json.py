#!/usr/bin/python3
"""contains the class_to_json function"""



def class_to_json(obj):
    """
    returns the dictionary description with simple data structure
    from json serialization of an object
    Args:
        obj: object
    """
    return obj.__dict__

    