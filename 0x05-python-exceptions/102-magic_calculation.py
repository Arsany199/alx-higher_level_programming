#!/usr/bin/python3

def magic_calculation(a, b):
    res = 0
    for i in range(3):
        try:
            if i > 3:
                raise Exception("Too far")
            else:
                res += a ** b / i
        except Exception:
            res = a + b
            break
    return res
