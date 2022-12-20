#!/usr/bin/python3
import dis


def magic_calculation(a, b):
    x = 0
    for i in range(a, b):
        try:
            if i > a:
                return x;
        except IndexError:
