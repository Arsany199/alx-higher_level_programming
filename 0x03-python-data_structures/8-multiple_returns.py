#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    first = sentence[0]
    if length <= 0:
        return None
    else:
        tuple_a = length, first
        return tuple_a
