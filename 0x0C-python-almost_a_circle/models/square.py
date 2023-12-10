#!/usr/bin/python3
"""Defines a class square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """this is the square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """initializing the square attributes"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """get the size of square"""
        return self.width

    @size.setter
    def size(self, value):
        """set the size of the square"""
        self.width = value
        self.height = value

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size)
