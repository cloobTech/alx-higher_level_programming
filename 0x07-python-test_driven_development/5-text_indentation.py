#!/usr/bin/python3

def text_indentation(text=None):
    """ a function that prints a text with 2 new lines
        after each of these characters: ., ? and :
    """
    if text is None:
        raise TypeError("text must be a string")
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        #delete white spaces at the start of text
        if (text[i] == " " and i == 0):
            while text[i] == " ":
                i += 1
                if (i == len(text) - 1):
                    return
        if text[i] in ".?:":
            print("{}{}".format(text[i], '\n'))
            if (i == len(text) - 1):
                return
            if text[i + 1] == " ":
                while text[i + 1] == " ":
                    i += 1
                    if ((i + 1) == len(text) - 1):
                        return
            i += 1
            continue
        print("{}".format(text[i]), end="")
        i += 1
