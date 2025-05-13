#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    dif = set()
    for el in set_1:
        if el not in set_2:
            dif.add(el)
    for el in set_2:
        if el not in set_1:
            dif.add(el)
    return dif
