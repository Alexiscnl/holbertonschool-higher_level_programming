#!/usr/bin/python3

def print_list_integer(my_list=[]):
    '''
    Fonction qui affiche chaque entier d'une liste sur une ligne séparée.
    :param my_list: Liste d'entiers (par défaut une liste vide).
    '''
    for x in my_list:
        print("{:d}".format(x))
