#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    idx = len(my_list)
    if idx == 0:
        print("{}".format("None"))
    else:
        for item in range(0, idx):
            idx -= 1
            print("{:d}".format(my_list[idx]))
