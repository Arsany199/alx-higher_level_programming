#!/usr/bin/python3
"""script that takes 2 arguments in order to solve this challenge"""
import requests
import sys

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(argv[2], argv[1])
    r = requests.get(url)
    commits = r.json()
    try:
        for ind in range(10):
            print("{}: {}".format(
                commits[ind].get("sha"),
                commits[ind].get("commit").get("author").get("name")))
    except IndexError:
        pass
