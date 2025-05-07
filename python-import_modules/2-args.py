#!/usr/bin/python3
import sys

if __name__ == "__main__":
    arguments = sys.argv[1:]
    count = len(arguments)

    if count == 0:
        print(f"0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print(f"{count} arguments:")
    for index, args in enumerate(arguments, 1):
        print(f"{index}: {args}")
