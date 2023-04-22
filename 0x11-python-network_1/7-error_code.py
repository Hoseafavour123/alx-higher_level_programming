#!/usr/bin/python3
"""Make HTTP request and handle exceptions"""
import sys
import requests
from requests.exceptions import HTTPError

if __name__ == '__main__':
    res = requests.get(sys.argv[1])
    if res.status_code >= 400:
        print("Error code: {}".format(res.status_code))
    else:
        print(res.text)
