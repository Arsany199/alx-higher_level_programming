#!/usr/bin/python3
"""find the peak in a list of ints"""

def find_peak(list_of_integers):
    my_max = None
    my_list = list_of_integers
    for i in my_list:
        if my_max is None or my_max < i:
            my_max = i
    return my_max
