#!/usr/bin/python3
"""define square"""


class Square:
    """represent square"""

    def __init__(self, size=0):
        """initializing the size of the square"""

        self.__size = size

    @property
    def size(self):
        """get size of square"""

        return self.__size

    @size.setter
    def size(self, value):
        """set size of square"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """area of square"""

        return self.__size ** 2
