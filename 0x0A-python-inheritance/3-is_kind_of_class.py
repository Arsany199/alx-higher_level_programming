#!/usr/bin/python3
"""Defines a function is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """function that return true or false obj instance to a_class"""
    if not isinstance(obj, a_class):
        return False
    return True
