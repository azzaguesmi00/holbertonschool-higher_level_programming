#!/usr/bin/python3
"""
This module contains a function that adds two integers.

"""

def add_integer(a, b=98):
    """
    Adds two integers.

    Parameters:
        a : The first integer or float.
        b : The second integer or float (default is 98).

    Returns:
        int: The sum of a and b, converted to an integer.

    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")

    return int(a) + int(b)
