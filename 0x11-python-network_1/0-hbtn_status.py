#!/usr/bin/python3
""" fetches data from https://alx-intranet.hbtn.io/status """
import urllib.request


url_obj = urllib.request.Request('https://alx-intranet.hbtn.io/status')
with urllib.request.urlopen(url_obj) as res:
    res = res.read()
    print("Body response:")
    print(f'\t- type: {type(res)}')
    print(f'\t- content: {res}')
    print(f'\t- utf8 content: {res.decode("utf-8")}')
