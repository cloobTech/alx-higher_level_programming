#!/usr/bin/python3
"""
that takes in a URL and an email, sends a POST request to the passed
URL with the email as a parameter, and displays the body
of the response (decoded in utf-8)
"""
import urllib.request
import urllib.parse
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    url_obj = urllib.request.Request(url, data)
    with urllib.request.urlopen(url_obj) as res:
        res = res.read()
        print(res.text)
