#!/usr/bin/python3
"""
containing student class
"""


class Student:
    """
    a func that defines a student
    public instance attributes:
    first_name -- str
    last_name -- str
    age -- int
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, att=None):
        """retrieve a dictionary representation of student"""
        if att is None:
            return self.__dict__
        else:
            stu = dict()
            for index in att:
                if index in self.__dict__.keys():
                    stu.update({index: self.__dict__[index]})
            return stu
