#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    list_len = len(my_list)
    if idx < 0 and idx >= list_len:
        return my_list
    for item in my_list:
        item_idx = my_list.index(item)
        if item_idx == idx:
            del my_list[item_idx]
    return my_list
