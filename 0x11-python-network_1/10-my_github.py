#!/usr/bin/python3
"""
a Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id"""
import sys
import requests


user_name = sys.argv[1]
password = sys.argv[2]
auth = requests.auth.HTTPBasicAuth(user_name, password)
url = f'https://api.github.com/user'

response = requests.get(url, auth=auth)
try:
    data = response.json()
    user_id = data.get('id')
    print(user_id)
except Exception as err:
    print('None')
