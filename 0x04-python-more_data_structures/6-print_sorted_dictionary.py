#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    if a_dictionary == None:
        return
    for key in sorted(a_dictionary.keys()):
        print("{} : {}".format(key, a_dictionary.get(key)))
