#!/usr/bin/python3
"""Defines a square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """the square class"""
    def __init__(self, size):
        """initialize the class attributes"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)


