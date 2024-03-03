#!/usr/bin/python3
"""containing the class "student" """

class student:
    """
    Representation of a student
    that defines a student
    public instance attributes:
    first_name -- str
    last_name -- str
    age -- int
    """
    
    
    def __init__(self , first_name, last_name, age):
        """Initializes the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
    def to_json(self):
        """returns a dictionnary representation of a student instance"""
        return self.__dict__
