#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    idx = len(my_list)
    for item in range(0, len(my_list)):
        idx -= 1
        print("{:d}".format(my_list[idx]))
