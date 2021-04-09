#!/usr/bin/python3
"""Polls given URL and displays X-Request-Id"""
from urllib import request
from sys import argv

with request.urlopen(argv[1]) as response:
    headers = response.info()
    print(headers.get("X-Request-Id"))
