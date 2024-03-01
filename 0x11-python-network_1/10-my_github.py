#!/usr/bin/python3
"""Sends a search request for a given string"""
import requests
import sys


if __name__ == "__main__":
    url = "https://swapi.co/api/people"
    param = {"search": sys.argv[1]}
    res = requests.get(url, param=param).json()

    print("Number of results: {}".format(res.get("count")))
    [print(r.get("name")) for r in res.get("results")]
