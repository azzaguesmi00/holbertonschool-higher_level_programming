#!/usr/bin/python3
"""Defines a Rectangle class"""


class Rectangle:
    """Rectangle class with private width and height attribute"""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle instance

        Args:
            width: The width of the rectangle Default is 0.
            height: The height of the rectangle Default is 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter method for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates and returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate and return the rectangle meter"""
        return 2 * (self.__width + self.__height)
