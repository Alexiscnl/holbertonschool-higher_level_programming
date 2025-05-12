#!/usr/bin/python3

def element_at(my_list, idx):
    """
    Récupère un élément d'une liste à un indice donné.
    :param my_list: La liste d'éléments.
    :param idx: L'indice de l'élément à récupérer.
    :return: L'élément si l'indice est valide, sinon None.
    """
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
