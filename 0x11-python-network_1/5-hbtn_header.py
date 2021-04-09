#!/usr/bin/python3
"""Fetch a given url and display X-Request-Id in the response header"""
import requests
from sys import argv

if __name__ == "__main__":
    response = requests.get(argv[1])
    print(response.headers.get("X-Request-Id"))
