#!/usr/bin/python3
"""Requests a URL and get the value of a variable"""
import sys
import urllib.request


if __name__ == '__main__':
    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as res:
        print(res.headers['X-Request-Id'])
