#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        First_char = None
    else:
        First_char = sentence[0]

        return (len(sentence), First_char)
