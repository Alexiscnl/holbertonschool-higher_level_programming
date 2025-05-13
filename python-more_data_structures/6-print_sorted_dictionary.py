#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = a_dictionary.keys()
    sort_keys = sorted(keys)
    for key in sort_keys:
        print(key, ":", a_dictionary[key])

