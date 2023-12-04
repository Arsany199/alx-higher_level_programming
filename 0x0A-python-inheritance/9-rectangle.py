#!/usr/bin/python3
"""Defines rectangle class inherits another class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """rectangle class inherited BaseGeometry"""
    def __init__(self, width, height):
        """initializing the width and the height"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """function that returns the area of rectangle"""
        return self.__height * self.__width

    def __str__(self):
        """function that returns this sentence"""
        return ("[Rectangle] " + str(self.__width) + "/" + str(self.__height))
