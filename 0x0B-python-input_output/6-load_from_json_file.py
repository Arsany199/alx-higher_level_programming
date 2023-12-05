#!/usr/bin/python3
"""Define that module that make an obj by json"""
import json


def load_from_json_file(filename):
    """function that creats obj from json"""
    with open(filename) as f:
        return json.load(f)
