#!/usr/bin/python3
""" that takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response
"""
import urllib.request
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    url_obj = urllib.request.Request(url)
    with urllib.request.urlopen(url_obj) as res:
        res = res.info()
        print(res.get('X-Request-Id'))
