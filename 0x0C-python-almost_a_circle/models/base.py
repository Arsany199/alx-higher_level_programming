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
        if list_dictionaries is None:
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

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """it returns instance with all attributes"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            elif cls.__name__ == "Square":
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """"""
        file_name = cls.__name__ + ".json"
        try:
            with open(file_name, mode="r", encoding="UTF8") as f:
                cont = cls.from_json_string(f.read())
        except:
            return []

        instances = []

        for i in cont:
            tmp = cls.create(**i)
            instances.append(tmp)
        return instances
