#!/usr/bin/python3
"""Define the rectangle class"""


class Rectangle:
    """my rectangle"""

    def __init__(self, width=0, height=0):
        """initialize the width and height"""

        self.width = width
        self.height = height

    @property
    def width(self):
        """get the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """function that sets the width of rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """function that gets the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """function that sets the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
