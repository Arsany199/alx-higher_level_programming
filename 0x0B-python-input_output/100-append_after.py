#!/usr/bin/python3
"""module defines insertion in a text file"""


def append_after(filename="", search_string="", new_string=""):
    """function that inserts a text after each line """
    t = ""
    with open(filename) as f:
        for line in f:
            t += line
            if search_string in line:
                t += new_string
    with open(filename, mode="w") as f2:
        f2.write(t)
