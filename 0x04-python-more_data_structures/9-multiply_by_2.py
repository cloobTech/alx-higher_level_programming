#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    b_dic = a_dictionary.copy()
    for key in b_dic:
        b_dic[key] *= 2
    return b_dic
