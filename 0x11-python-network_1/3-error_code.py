#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8).
"""
import urllib.request
import urllib.error
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    url_obj = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(url_obj) as res:
            print(res.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f'Error code: {e.code}')
