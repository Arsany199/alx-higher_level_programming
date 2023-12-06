#!/usr/bin/python3
"""Module defines the function print_status"""
import sys


def print_status():
    """function that prints the status of the request"""
    c = 0
    s = 0
    fs = 0
    sc = {"200": 0, "301": 0, "400": 0, "401": 0,
                    "403": 0, "404": 0, "405": 0, "500": 0}

    for lin in sys.stdin:
        line = lin.split()
        try:
            s += int(line[-1])
            code = line[-2]
            sc[code] += 1
        except:
            continue
        if c == 9:
            print("File size: {}".format(s))
            for k, v in sorted(sc.items()):
                if (v != 0):
                    print("{}: {}".format(k, v))
            c = 0
        c += 1
    if c < 9:
        print("File size: {}".format(s))
        for k, v in sorted(sc.items()):
            if (v != 0):
                print("{}: {}".format(k, v))


if __name__ == "__main__":
    print_status()
