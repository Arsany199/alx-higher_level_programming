#!/usr/bin/python3
"""Define module that append text"""


def append_write(filename="", text=""):
    """function that append text in the file"""
    with open(filename, "a", encoding="utf-8") as f:
        return (f.write(text))
