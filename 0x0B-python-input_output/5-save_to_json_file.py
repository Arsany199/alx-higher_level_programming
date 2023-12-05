#!/usr/bin/python3
"""Define module that use json to write an obj in file"""
import json


def save_to_json_file(my_obj, filename):
    """function that writes an obj in text file using json"""
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
