#!/usr/bin/python3
"""This module is the base module"""
import json
import csv


class Base:
    """Class that manage the id of the attributes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initializing the attributes"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """turns the dict into json"""
        if list_dictionaries == [] or list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save the file string serialization as json"""
        file_name = cls.__name__ + ".json"
        with open(file_name, mode="w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                f.write(Base.to_json_string(list_dicts))
