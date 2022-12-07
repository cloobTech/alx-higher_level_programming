#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if  my_list == None:
        return
    idx = len(my_list)
    for item in range(0, idx):
        idx -= 1
        print("{:d}".format(my_list[idx]))
