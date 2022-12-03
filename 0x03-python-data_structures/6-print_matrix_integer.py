#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix[0] == []:
        print("{}".format('\n'), end="")
    for i in matrix:
        for j in i:
            if i.index(j) < (len(i) - 1):
                print("{:d} ".format(j), end="")
            else:
                print("{:d}".format(j), end="\n")
