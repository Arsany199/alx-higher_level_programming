#!/usr/bin/python3
"""send a post request to a url, show response after"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    v = {"email": sys.argv[2]}
    r = requests.post(url, data=v)
    print(r.text)
