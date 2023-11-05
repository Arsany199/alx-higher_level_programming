#!/usr/bin/python3
def multiple_returns(sentence):
    tuple_a = ()
    length = len(sentence)
    first = sentence[0]
    if len(sentence) == 0:
        return first == 0, "None"
    else:
        tuple_a = length, first
        return tuple_a
