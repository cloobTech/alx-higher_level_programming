#!/usr/bin/python3
"""a Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys


if __name__ == '__main__':
    if len(sys.argv) == 2:
        q = sys.argv[1]
    else:
        q = ""
    payload = {'q': q}
    url = 'http://0.0.0.0:5000/search_user'
    response = requests.post(url, data=payload)
    try:
        res_json = response.json()
        if res_json:
            print(f'[{res_json.get("id")}] {res_json.get("name")}')
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
