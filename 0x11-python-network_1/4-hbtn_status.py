#!/usr/bin/python3
"""Make HTTP request to URL"""
import requests


if __name__ == '__main__':
    resp = requests.get("https://alx-intranet.hbtn.io/status")
    text = resp.text

    print("Body response:")
    print("\t- type: {}".format(type(text)))
    print("\t- content: {}".format(text))
