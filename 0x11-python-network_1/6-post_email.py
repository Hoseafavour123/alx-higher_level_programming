#!/usr/bin/python3
"""Post an email"""
import sys
import requests


if __name__ == '__main__':
    url = sys.argv[1]
    val = sys.argv[2]

    res = requests.post(url, data={'email': val})
    print(res.text)
