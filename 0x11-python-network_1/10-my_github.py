#!/usr/bin/python3
"""Fetches the GitHub Id of a given token"""
import requests
from sys import argv

user = argv[1]
pwd = argv[2]

headers = {'Accept': 'application/vnd.github.v3+json'}
url = "http://api.github.com/users/{}".format(user)

response = requests.get(url, auth=(user, pwd), headers=headers)
json = response.json()

if 'id' in json:
    print(json.get('id'))
else:
    print('None')
