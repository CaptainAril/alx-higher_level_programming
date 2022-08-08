#!/usr/bin/python3
"""This module defines a text indenting function."""


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0

    while i < len(text):
        print(text[i], end="")
        if text[i] in ".?:" and i < len(text) - 1:
            print('\n')
            i += 1
            if text[i] == " ":
                i += 1
            continue
        i += 1
