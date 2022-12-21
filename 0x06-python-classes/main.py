#!/usr/bin/python3
Square = __import__('6-square').Square
print("Hello")
try:
    my_square = Square(3, 0)
except Exception as e:
    print(e)
