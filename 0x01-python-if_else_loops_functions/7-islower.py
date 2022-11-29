#!/usr/bin/python3

def islower(c):
    if ord(c) >= 97 and ord(c) <= 122:
        print("{} is lower".format(c))
    else:
        print("{} is upper".format(c))
