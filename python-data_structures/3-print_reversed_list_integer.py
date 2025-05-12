#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """
    Affiche tous les entiers d'une liste dans l'ordre inverse, un par ligne.
    """
    my_list = my_list[::-1]

    for element in my_list:
        print("{:d}".format(element))
