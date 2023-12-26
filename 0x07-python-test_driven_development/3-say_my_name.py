#!/usr/bin/python3
"""Module contains function that prints to stdout"""


def say_my_name(first_name, last_name=""):
    """Function prints My name is <first name> <last name>"""
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    elif type(last_name) != str:
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
