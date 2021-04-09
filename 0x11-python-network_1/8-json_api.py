#!/usr/bin/python3
"""Sends a POST request with a letter as parameter"""
import requests
from sys import argv

if __name__ == "__main__":
    try:
        param = argv[1]
    except:
        param = ""

    url = "http://0.0.0.0:5000/search_user"

    response = requests.post(url, data={'q': param})
    try:
        json = response.json()
        if 'id' in json:
            print("[{}] {}".format(json.get("id"), json.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
