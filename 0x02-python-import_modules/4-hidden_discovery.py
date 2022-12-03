#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4
    items = dir(hidden_4)
    for item in items:
        if (item[0] and item[1]) == "_":
            continue
        print(item)
