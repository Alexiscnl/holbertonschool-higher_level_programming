#!/usr/bin/python3
import sys

arguments = sys.argv[1:]
total = 0

for index, value in enumerate(arguments):
    total += int(value)
print(total)
