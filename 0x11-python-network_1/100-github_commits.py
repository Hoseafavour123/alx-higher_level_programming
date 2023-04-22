#!/usr/bin/python3
"""Gets a list of commits using github api"""
from sys import argv
import requests


if __name__ == '__main__':
    url = 'https://api.github.com/repos/{}/{}/commits'.format(argv[2], argv[1])
    res = requests.get(url)
    commits = res.json()
    for commit in commits[:10]:
        print(commit.get('sha'), end=': ')
        print(commit.get('commit').get('author').get('name'))
