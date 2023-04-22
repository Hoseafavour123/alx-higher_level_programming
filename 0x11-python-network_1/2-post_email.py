#!/usr/bin/python3
"""Post an email"""
import sys
import urllib.parse
import urllib.request


if __name__ == '__main__':
    url = sys.argv[1]
    val = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(val).encode("ascii")

    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
