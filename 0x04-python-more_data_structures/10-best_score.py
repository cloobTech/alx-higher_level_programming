#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    max = 0
    count = 0
    for k in a_dictionary:
        if a_dictionary[k] > max:
            max = a_dictionary[k]
            count += 1
    lis = list(a_dictionary.values()).index(max)
    key = list(a_dictionary.keys())
    if count == 0:
        return None
    return (key[lis])
