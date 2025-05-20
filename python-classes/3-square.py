#!/usr/bin/python3
"""
Module 2-square
Définit une classe Square avec un attribut privé size,
et un constructeur avec vérification de type et de valeur.
"""


class Square:

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size * self.__size
