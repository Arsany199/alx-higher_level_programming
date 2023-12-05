#!/usr/bin/python3
"""Define a module that has a student class"""


class Student:
    """A student class"""
    def __init__(self, first_name, last_name, age):
        """initializing the attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """function that returns the dictionary"""
        if type(attrs) == list and all(type(ele) == str for ele in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return (self.__dict__)

    def reload_from_json(self, json):
        """function that replace the attributes of student"""
        for k, v in json.item():
            setattr(self, k, v)
