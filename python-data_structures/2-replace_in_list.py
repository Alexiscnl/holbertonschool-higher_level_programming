#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """
    Remplace un élément dans une liste à un indice donné.
    :param my_list: La liste d'origine.
    :param idx: L'indice où l'élément doit être remplacé.
    :param element: La nouvelle valeur à insérer.
    :return: La liste mise à jour ou la liste d'origine si l'indice est invalide.
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element

    return my_list
