#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = []
    for i in range(0, len(my_list)):
        if search > len(my_list):
            return my_list
        new_list.append(my_list[i])
        if i + 1 == search:
            new_list[i] = replace
    return new_list
