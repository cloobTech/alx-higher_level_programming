#!/usr/bin/python3

for i in range(0, 10):
    for j in range(1, 10):
        if i == j or j < i:
            continue
        if i == 8 and j == 9:
            print("{num_1}{num_2}".format(num_1=i, num_2=j))
        else:
            print("{num_1}{num_2}, ".format(num_1=i, num_2=j), end="")
