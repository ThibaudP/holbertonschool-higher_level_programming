#!/usr/bin/python3
"""Fetch a given url and display X-Request-Id in the response header"""
import requests
from sys import argv

response = requests.get(argv[1])
if response.status_code < 400:
    print(response.text)
else:
    print("Error code: {}".format(response.status_code))
