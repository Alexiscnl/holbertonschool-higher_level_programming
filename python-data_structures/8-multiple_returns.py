#!/usr/bin/python3

def multiple_returns(sentence):
    lenght = len(sentence)
    if len(sentence) == 0:
        return (0, None)
    first_chr = sentence[0]
    return (lenght, first_chr)
