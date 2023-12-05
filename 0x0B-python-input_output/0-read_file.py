#!/usr/bin/python3
"""module that reads a file"""


def read_file(filename=""):
    """function opens a file and reads its content"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
