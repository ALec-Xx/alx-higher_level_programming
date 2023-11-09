#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dic_sort = sorted(a_dictionary)
    for k in dic_sort:
        print("{}: {}".format(k, str(a_dictionary[k])))
