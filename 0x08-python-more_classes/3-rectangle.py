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

    def area(self):
        """function that return the area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """function return the perimeter of the rectangle"""
        if self.__width == 0 or self.height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)
        self.__width = value

    def __str__(self):
        """return a rectangle with # character"""
        if self.__width == 0 or self.__height == 0:
            return ("")

        rec = []
        for i in range(self.__height):
            [rec.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rec.append("\n")
        return ("".join(rec))

    def __repr__(self):
        """return the string of the rectangle"""
        rec = "Rectangle(" + str(self.__width)
        rec += ", " + str(self.__height) + ")"
        return rec
