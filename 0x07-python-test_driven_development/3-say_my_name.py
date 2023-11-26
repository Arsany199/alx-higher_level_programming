#!/usr/bin/python3
"""Define function that print names"""



def say_my_name(first_name, last_name=""):
    """this function print the first name and the last name

    args:
        first_name: the first name
        last_name: the last name

    raise :
        TypeError: if the names were not strings

    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
