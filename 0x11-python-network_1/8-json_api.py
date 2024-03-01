#!/usr/bin/python3
""" script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter"""
import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"

    if len(sys.argv) < 2:
        search = {'q': '""'}
    else:
        search = {'q': sys.argv[1]}
    req = requests.post(url, search)
    try:
        search = req.json()
    except ValueError:
        print("Not a valid JSON")
    else:
        if hasattr(search, '__contains__') and len(search) < 1:
            print("No result")
        else:
            print("[{}] {}".format(search['id'], search['name']))
