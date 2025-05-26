#!/usr/bin/python3

def is_same_class(obj, a_class):
    """
    Retourne True si obj est exactement une instance de a_class,
    sinon False.
    """
    return type(obj) == a_class
