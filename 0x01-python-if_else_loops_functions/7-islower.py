#!/usr/bin/python3
def islower(c):
    """
        Function checks for lowercase letter, returns true if found

        :param c: alphabet as argument
    """
    if ord(c) >= 97 and ord(c) < 123:
        return True
    else:
        return False
