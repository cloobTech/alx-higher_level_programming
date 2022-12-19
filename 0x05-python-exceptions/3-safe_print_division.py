#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        c = a / b
    except(ZeroDivisionError, NameError, TypeError):
        c = None
    finally:
        print("Inside result: {}".format(c))
