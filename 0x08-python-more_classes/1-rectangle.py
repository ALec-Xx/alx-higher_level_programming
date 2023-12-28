#!/usr/bin/python3
"""Module contains class that defines rectangle"""


class Rectangle:
    """class defines a rectangle"""
    def __init__(self, width=0, height=0):
        """Initialization of various class objects.

        Args:
            width - rectangle width or breadth
            height - rectangle height
        """
        self.__height = height
        self.__width = width

    @property
    def height(self):
        """property to retrieve height value"""
        return self.__height

    @property
    def width(self):
        """property to retrieve width value"""
        return self.__width

    @height.setter
    def height(self, value):
        """property to set height value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @width.setter
    def width(self, value):
        """property to set width value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
