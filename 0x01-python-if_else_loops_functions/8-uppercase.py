#!/usr/bin/python3
def uppercase(str):
    """
        Function that prints string in uppercase followed by new line.

        :param str: str argument to print.
    """
    for char in str:
        if (ord(char) >= 97 and ord(char) < 123):
            char = chr(ord(char) - 32)
        print("{:s}".format(char), end='')
    print()
