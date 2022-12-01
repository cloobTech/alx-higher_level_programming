#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    av = sys.argv
    if len(av) <= 1:
        print("0 arguments.")
    elif len(av) == 2:
        print("1 argument:")
    else:
        print("{} arguments:".format(len(av) - 1))
    for i in av:
        if av.index(i) == 0:
            continue
        print("{}: {}".format(av.index(i), i))
