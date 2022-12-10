#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    k = sorted(a_dictionary)
    for a in k:
        print("{}: {}".format(a, a_dictionary[a]))
