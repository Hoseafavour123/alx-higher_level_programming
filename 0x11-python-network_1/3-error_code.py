#!/usr/bin/python3
"""Make URL request and manage exceptions"""
import sys
import urllib.request

if __name__ == '__main__':
    url = sys.argv[1]

    req = urllib.request.Request(url)

    try:
        with urllib.request.urlopen(url) as res:
            print(res.read().decode('utf-8'))

    except urllib.error.HTTPError as er:
        print("Error code: {}".format(er.code))
