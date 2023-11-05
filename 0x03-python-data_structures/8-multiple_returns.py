#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence != "":
        first = sentence[0]
    else:
        first = None
    my_tuple = (len(sentence), first)
    return my_tuple
