#!/usr/bin/python3
"""Polls an URL and returns the content, or the error code in case of error"""
from urllib import request, parse, error
from sys import argv

try:
    with request.urlopen(argv[1]) as response:
        html = response.read()
        print(html.decode('utf-8'))
except error.HTTPError as error:
    print("Error code: {}".format(error.code))
