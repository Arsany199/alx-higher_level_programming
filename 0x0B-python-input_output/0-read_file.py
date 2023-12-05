#!/usr/bin/python3
"""module that reads a file"""


def read_file(filename=""):
    """function that read the content of a file"""
    with open("my_file_0.txt", "r",  encoding="utf-8") as fil:
        print(fil.read(), end="")
