#!/usr/bin/python3
"""Define the rectangle class"""


class Rectangle:
    """my rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """initialize the width and height"""

        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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
        if self.__width == 0 or self.height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)
        self.__width = value

    def __str__(self):
        """return a rectangle with # character"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        rec = ""
        for i in range(self.__height):
            for j in range(self.__width):
                rec += "#"
            if i < self.__height - 1:
                rec += "\n"
        return rec

    def __repr__(self):
        """return the width and height of the rec"""
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        """function that print msg when rec deleted"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
