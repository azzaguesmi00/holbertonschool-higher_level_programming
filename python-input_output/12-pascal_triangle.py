#!/usr/bin/python3
"""
    file containing student class
"""


def pascal_triangle(n):
    """
    a func that defines a student
    public instance attributes:
    first_name -- str
    last_name -- str
    age -- int
    """
    the_list = [[1]]
    if n <= 0:
        return []
    for i in range(1, n):
        case_list = [1]
        for k in range(1, i):
            case_list.append(the_list[i - 1][k - 1] + the_list[i - 1][k])
        case_list.append(1)
        the_list.append(case_list)
    return the_list
