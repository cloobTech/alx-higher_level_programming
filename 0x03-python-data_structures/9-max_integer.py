#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    mx_num = my_list[0]
    for num in my_list:
        if num > mx_num:
            mx_num = num
    return mx_num
