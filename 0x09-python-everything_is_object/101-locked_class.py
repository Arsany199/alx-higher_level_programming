#!/usr/bin/python3
"""Define a function lockedClass"""


class LockedClass:
    """function that prevent from creating new attribute except first_name"""
    __slots__ = ["first_name"]
