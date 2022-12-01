#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    add_cl = 0
    av = sys.argv
    n = len(av)
    for i in range(1, n):
        if len(av) == 1:
            continue
        add_cl += int(av[i])
    print(add_cl)
