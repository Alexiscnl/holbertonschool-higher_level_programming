#!/usr/bin/python3
def common_elements(set_1, set_2):
    common = set()
    for el in set_1:
        if el in set_2:
            common.add(el)
    return common
