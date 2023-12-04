#!/usr/bin/python3
"""Defines the MyInt class"""


class MyInt(int):
    """MyInt class that inherits int class"""
    def __eq__(self, value):
        """function that make the equal ...not equal"""
        return self.real != value

    def __ne__(self, value):
        """function that make the not equal ...equal"""
        return self.real == value
