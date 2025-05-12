#!/usr/bin/python3

def multiple_returns(sentence):
    lenght = len(sentence)
    first_chr = sentence[0]
    if len(sentence) == 0:
        return (0, None)
    else:
        return (lenght, first_chr)
