#!/usr/bin/python3
for i in range(0, 100):
    if i / 10 == 9.9 and i % 10 == 9:
        print(i)
    else:
        print("{:02d}, ".format(i), end="")
