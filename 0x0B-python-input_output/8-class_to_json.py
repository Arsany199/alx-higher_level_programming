#!/usr/bin/python3
"""Define module has function class_to_json"""


def class_to_json(obj):
    """function that return the dictionary description"""
    return (obj.__dict__)
