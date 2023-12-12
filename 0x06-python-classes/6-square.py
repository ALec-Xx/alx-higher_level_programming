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
        """Property to retrieve instance attribute"""
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
        """Property setter to set instance attribute"""
        try:
            value[0] and len(value) == 2
        except TypeError:
            print("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Returns current area"""
        return self.__size**2

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print("")
            return
        else:
            for i in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                [print(" ", end="") for k in range(self.__position[0])]
                [print("#", end="") for j in range(self.__size)]
                print("")
