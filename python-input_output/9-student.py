#!/usr/bin/python3
"""
    file input-output
"""


class Student:
    """
    a function that defines a student
    public instance attributes:
    first_name -- str
    last_name -- str
    age -- int
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieve a dictionary representation of student"""
        return self.__dict__
