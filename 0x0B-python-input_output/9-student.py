#!/usr/bin/python3
"""Define a module that has a student class"""


class Student:
    """A student class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """function that returns the dictionary"""
        return (self.__dict__)
