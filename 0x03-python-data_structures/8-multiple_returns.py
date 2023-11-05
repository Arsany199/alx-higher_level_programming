#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    first = sentence[0]
    if len(sentence) == 0:
        return first is None
    else:
        my_tuple = length, first
        return my_tuple
