#!/usr/bin/python3
"""module contains addition function"""


def add_integer(a, b=98):
    """function adds two integers"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
