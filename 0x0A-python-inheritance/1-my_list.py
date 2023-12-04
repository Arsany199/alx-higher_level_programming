#!/usr/bin/python3
"""Defines the class MyList"""


class MyList(list):
    """class mylist inheritance of the class list"""

    def print_sorted(self):
        """function that prints the list sorted"""

        print(sorted(self))
