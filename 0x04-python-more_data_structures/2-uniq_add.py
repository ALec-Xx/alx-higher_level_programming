#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq = set()
    add_uniq = lambda x: uniq.add(x) or x
    uniq_num = map(add_uniq, my_list)
    return sum(uniq_num)
