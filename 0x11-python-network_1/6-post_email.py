#!/usr/bin/python3
"""Fetch a given url and display X-Request-Id in the response header"""
import requests
from sys import argv

response = requests.post(argv[1], data={'email': argv[2]})
print(response.text)
