#!/usr/bin/python3
"""Module contains function that prints modified text"""


def text_indentation(text):
    """Function prints a text with 2 new lines 
    after each of these characters: ., ? and :

    Args:
        text - written string of words
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    newLine_char = ['.', '?', ':']
    currentLine = ""
    for char in text:
        currentLine += char
        if char in newLine_char:
            print(currentLine.strip())
            print()
            currentLine = ""
    if currentLine:
        print(currentLine.strip())
