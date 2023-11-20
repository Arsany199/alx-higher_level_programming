#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError:
        print("Exeption: {}".format(ValueError), file=sys.stderr)
        return False
    except TypeError:
        print("Exeption: {}".format(TypeError), file=sys.stderr)
        return False
