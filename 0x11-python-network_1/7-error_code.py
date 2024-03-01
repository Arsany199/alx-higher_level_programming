#!/usr/bin/python3
"""HTTP status code is greater than or equal to 400, print: Error code:
followed by the value of the HTTP status code"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    myresp = requests.get(url)
    if myresp.status_code >= 400:
        print("Error code: {}".format(myresp.status_code))
    else:
        print(myresp.text)
