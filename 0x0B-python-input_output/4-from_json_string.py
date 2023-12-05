#!/usr/bin/python3
"""Define module that use json"""
import json


def from_json_string(my_str):
    """function that use json to represent obj"""
    return json.loads(my_str)
