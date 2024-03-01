#!/usr/bin/python3
"""script url fetching script in python"""

import requests

url = 'https://intranet.hbtn.io/status'


if __name__ == '__main__':
    requ = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(requ.text)))
    print("\t- content: {}".format(requ.text))
