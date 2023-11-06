#!/usr/bin/python3
def no_c(my_string):
    list_str = []
    new_str = ""
    for char in my_string:
        list_str.append(char)
    for elem in list_str:
        if elem == "c" or elem == "C":
            list_str.remove(elem)
    for char in list_str:
        new_str += str(char)
    return new_str
            
