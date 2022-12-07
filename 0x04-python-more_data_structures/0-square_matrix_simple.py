#!/usr/bin/python3
def power(n):
    return n * n


def square_matrix_simple(matrix=[]):
    new_matrix = []
    mx = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            new_matrix = map(power, matrix[i])
        mx.append(list(new_matrix))
    return mx
