#!/usr/bin/python3

"""define the square"""


class Square:
    """represent a square"""

    def __init__(self, size=0):
        """initializing the size of the square"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size


    def area(self):
        """the area of the square"""

        return self.__size * self.__size
