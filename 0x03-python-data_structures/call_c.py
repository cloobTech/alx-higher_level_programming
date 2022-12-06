#!/usr/bin/python3

import ctypes

lib = ctypes.CDLL('./libAbj.so')
lib.print_prod(4, 4)
