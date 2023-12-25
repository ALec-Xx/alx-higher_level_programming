#!/usr/bin/python3
"""Module defines square class"""


class Square:
    """class Square that defines a square by:

    Attributes:
        size(int): private instance attribute
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initialization function creating instance attribute"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """property to retrieve attribute"""
        return self.__size

    @property
    def position(self):
        """property to retrieve position"""
        return self.__position

    @size.setter
    def size(self, size):
        """property setter to set instance attribute"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @position.setter
    def position(self, value):
        """property setter to set position"""
        if not isinstance(value, tuple) or len(value) != 2 or\
                not all(isinstance(i, int) for i in value) or\
                not all(i >= 0 for i in value):
                    raise TypeError("position must be a tuple \
                            of 2 positive integer")
        self.__position = value

    def area(self):
        """Returns current area"""
        return self.__size**2

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" + self.__size)

    def __str__(self):
        """Define the print() representation of a Square"""
        if self.__size != 0:
            [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            if i != self.__size - 1:
                print("")
        return ("")
