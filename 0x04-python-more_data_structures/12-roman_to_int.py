#!/usr/bin/python3
def roman_to_int(roman_string):
    ret = 0
    for value in roman_string:
        if value == "I":
            ret += 1
        elif value == "V":
            ret += 5
        elif value == "X":
            ret += 10
        elif value == "L":
            ret += 50
        elif value == "C":
            ret += 100
        elif value == "D":
            ret += 500
        elif value == "M":
            ret += 1000
        else:
            return None
    return ret
