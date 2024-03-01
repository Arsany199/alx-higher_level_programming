#!/usr/bin/python3
"""return header from the url"""
from sys import argv
import requests

if __name__=="__main__":
    res = requests.get(sys.argv[1])
    print(res.headers.get("X-Request-Id"))
