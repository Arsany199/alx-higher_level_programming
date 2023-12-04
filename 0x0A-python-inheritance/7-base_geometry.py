#!/usr/bin/python3
"""Defines class BaseGeometry"""


class BaseGeometry:
    """Represent the BaseGeometry class"""
    pass

    def area(self):
        """function of area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """function that validates parameter"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
