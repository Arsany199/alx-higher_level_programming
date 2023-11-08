#!/usr/bin/python3

def weight_average(my_list=[]):
    if my_list == [] or my_list is None:
        return 0
    else:
        result = 0
        result2 = 0
        for x, y in my_list:
            result += x * y
            result2 += y
        return result / result2
