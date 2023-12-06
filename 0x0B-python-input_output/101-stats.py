#!/usr/bin/python3
"""Module defines the function print_stats"""
if __name__ = "__main__":
    import sys


def print_stats(size, status_codes):
    """function that prints the status of the request"""

    print("File size: {}".format(size))
    for key in sorted(status_codes):
        print("{}: {}".format(key, status_codes[key]))

    size = 0
    status_codes = {}
    v_c = ['200', '301', '400', '401', '403', '404', '405', '500']
    i = 0

    try:
        for line in sys.stdin:
            if i == 10:
                print_stats(size, status_codes)
                i = 1
            else:
                i += 1

            line = line.split()

            try:
                size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in v_c:
                    if status_codes.get(line[-2], -1) == -1:
                        status_codes[line[-2]] = 1
                    else:
                        status_codes[line[-2]] += 1
            except IndexError:
                pass

        print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise
