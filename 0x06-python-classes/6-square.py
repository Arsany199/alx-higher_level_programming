#!/usr/bin/python3
"""define square"""


class Square:
    """represent square"""

    def __init__(self, size=0, position=(0, 0)):
        """initializing the size of the square"""

        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """get the position of the square"""

        return self.__position

    @position.setter
    def position(self, value):
        """set the position of the square"""

        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """area of square"""

        return self.__size ** 2

    def my_print(self):
        """print the squares in #"""

        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
