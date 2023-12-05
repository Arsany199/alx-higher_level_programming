#!/usr/bin/python3
"""Defines a module that json an obj"""
import json


def to_json_string(my_obj):
    """function that returns json representayion of an obj"""
    return json.dumps(my_obj)
