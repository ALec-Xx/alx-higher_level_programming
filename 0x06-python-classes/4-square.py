#!/usr/bin/python3
"""Module defines square class"""

class Square:
    """class Square that defines a square by:

    Attributes:
        size(int): private instance attribute
    """
    def __init__(self, size=0):
        """Initialization function creating instance attribute"""
        self.__size = size

    @property
    def size(self):
        """property to retrieve attribute"""
        return self.__size

    @size.setter
    def size(self, size):
        """property setter to set instance attribute"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Returns current area"""
        return self.__size**2
