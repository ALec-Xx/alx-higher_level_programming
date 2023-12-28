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

    def area(self):
        """Returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __del__(self):
        """Prints message when instance of Rectangle is deleted"""
        print(f"Bye rectangle...")

    def __str__(self):
        """print rectangle with character #"""
        rectangle = ""
        if self.__width == 0 or self.__height == 0:
            return ""
        for i in range(self.__height):
            rectangle += "#" * self.__width + "\n"
        return rectangle.rstrip()

    def __repr__(self):
        """return a string representation of the rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"
