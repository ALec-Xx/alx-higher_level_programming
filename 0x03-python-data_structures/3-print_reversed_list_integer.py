#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    l_list = len(my_list) - 1
    for i in my_list:
        print("{}".format(my_list[l_list]))
        l_list -= 1
