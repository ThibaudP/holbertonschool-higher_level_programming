#!/usr/bin/python3
"""Sends a POST request to a given URL with an email as parameter"""
from urllib import request, parse
from sys import argv

url = argv[1]
values = {'email': argv[2]}
data = parse.urlencode(values)
data = data.encode('ascii')
req = request.Request(url, data)

with request.urlopen(req) as response:
    html = response.read()
    print(html.decode('utf-8'))
