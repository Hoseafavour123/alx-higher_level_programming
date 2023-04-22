#!/usr/bin/python3
"""Make HTTP request and get header value"""
import requests
import sys


if __name__ == '__main__':
    res = requests.get(sys.argv[1])
    print(res.headers['X-Request-Id'])
