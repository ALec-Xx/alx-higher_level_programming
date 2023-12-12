#!/usr/bin/python3
"""Module defines square class"""


class Square:
    """class Square that defines a square by:

    Attributes:
        size(int): private instance attribute
    """
    def __init__(self, size=0):
        """Initialization function creating instance attribute"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
