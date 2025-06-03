#!/usr/bin/python3
"""
Executable script using the Python 3 interpreter.

This shebang allows the script to be run directly from the terminal
without needing to explicitly call 'python3'.
"""


def read_file(filename=""):
    """
    Lit un fichier texte en UTF-8 et affiche son contenu dans la console.

    Args:
        filename (str): Le nom du fichier à lire. Par défaut, une chaîne vide.
    """
    with open(filename, "r", encoding="UTF-8")as f:
        print(f.read().strip('\n'), end="")
