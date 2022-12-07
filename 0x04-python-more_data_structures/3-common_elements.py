#!/usr/bin/python3

def common_elements(set_1, set_2):
    new_list = []
    dup_list = []
    my_list = (list(set_1) + list(set_2))
    for item in my_list:
        if item not in new_list:
            new_list.append(item)
        else:
            dup_list.append(item)
    return set(dup_list)
