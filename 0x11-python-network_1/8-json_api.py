#!/usr/bin/python3
"""Makes a posts requests and confirms json type"""
import sys
import requests


if __name__ == '__main__':
    q = sys.argv[1] if len(sys.argv) == 2 else ""
    res = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})

    try:
        res_dict = res.json()
        id, name = res_dict.get('id'), res_dict.get('name')
        if len(res_dict) == 0 or not id or not name:
            print("No result")
        else:
            print("[{}] {}".format(res_dict.get('id'), res_dict.get('name')))
    except:
        print("Not a valid JSON")
