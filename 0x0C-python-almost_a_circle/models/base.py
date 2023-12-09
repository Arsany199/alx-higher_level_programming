#!/usr/bin/python3
"""This module is the class module"""


class Base:
    """Class that manage the id of the attributes"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
