#!/usr/bin/python3
"""Defines function inherits_from"""


def inherits_from(obj, a_class):
    """function return true or false if obj is instance 
    of class inherted directly or in directly"""
    if issubclass(type(obj), a_class) and type(obj) == a_class:
        return False
    return True
