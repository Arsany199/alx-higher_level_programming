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

    def update(self, *args, **kwargs):
        """updating the square"""
        if len(args):
            for i, ar in enumerate(args):
                if i == 0:
                    self.id = ar
                if i == 1:
                    self.size = ar
                if i == 2:
                    self.x = ar
                if i == 3:
                    self.y = ar
        else:
            for k, v in kwargs.items():
                if hasattr(self, k) is True:
                    setattr(self, k, v)

    def __str__(self):
        """print the string of the square class"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size)

    def to_dictionary(self):
        """return the dictionary of square class"""
        return {"id": self.id,
                "x": self.x,
                "size": self.size,
                "y": self.y}
