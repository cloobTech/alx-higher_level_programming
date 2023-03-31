#!/usr/bin/python3
""" a Python script that fetches https://alx-intranet.hbtn.io/status"""
import requests


url = 'https://alx-intranet.hbtn.io/status'
result = requests.get(url)
print('Body response:')
print(f'\t- type: {type(result)}')
print(f'\t- content: {result.content}')
