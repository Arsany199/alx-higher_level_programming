#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    first = sentence[0]

    if sentence == "":
        return first == None
    else:
        return length, first
