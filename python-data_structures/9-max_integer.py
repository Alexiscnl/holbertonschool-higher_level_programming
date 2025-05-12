#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    max_value = my_list[0]
    for el in my_list:
        if el > max_value:
            max_value = el
    return max_value
