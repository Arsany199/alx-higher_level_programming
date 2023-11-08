#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    for x in sorted(a_dictionary.keys()):
        v = a_dictionary[x]
        print("{:s}: {}".format(x, v))

