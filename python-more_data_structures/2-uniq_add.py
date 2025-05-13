#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    for el in my_list:
        if el not in new_list:
            new_list.append(el)
    somme = sum(new_list)
    return somme
