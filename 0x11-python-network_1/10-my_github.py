#!/usr/bin/python3
"""Obtain gitbub id from github API with HTTP Authentication"""
import requests
from requests.auth import HTTPBasicAuth
from sys import argv


if __name__ == '__main__':
    url = 'https://api.github.com/users/{}'.format(argv[1])
    res = requests.get(url, auth=HTTPBasicAuth(argv[1], argv[2]))
    print(res.json().get('id'))
