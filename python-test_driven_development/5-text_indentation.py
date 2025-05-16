#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    temp = ""
    for i in text:
        temp += i
        if i in '.:?':
            print(temp.strip())
            print()
            temp = ""
    if temp.strip():
        print(temp.strip(), end="")
