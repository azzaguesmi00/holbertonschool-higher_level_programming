#!/usr/bin/python3
"""inheritance from BaseGeometry"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """A class to represent a rectangle."""


    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__height = height
        self.__width = height


# def area(self):
#    raise Exception("area() is not implemented")

# def integer_validator(self, name, value):
#    if type(value) is not int:
#        raise TypeError(f"{name} must be an integer")
#    if value < 1:
#        raise ValueError(f"{name} must be greater than 0")