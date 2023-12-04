#!/usr/bin/python3
"""defines a function is_same_class"""


def is_same_class(obj, a_class):
    """function that return true or false if the obj is a_class or not"""
    if type(obj) != a_class:
        return False
    return True
