#!/usr/bin/python3
"""module that write in a file"""


def write_file(filename="", text=""):
    """funcyion that write strings in files"""
    with open(filename, "w", encoding="utf-8") as f:
        return (f.write(text))
