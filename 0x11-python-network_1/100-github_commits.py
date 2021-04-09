#!/usr/bin/python3
"""Fetches the 10 latest commits from a given repo"""
import requests
from sys import argv

if __name__ == "__main__":
    repo = argv[1]
    owner = argv[2]

    h = {'Accept': 'application/vnd.github.v3+json'}
    u = "http://api.github.com/repos/{}/{}/commits".format(owner, repo)

    response = requests.get(url=u, params={'per_page': 10}, headers=h)
    json = response.json()
    for commit in json:
        print("{}: {}".format(commit.get("sha"),
                              commit.get("commit").get("author").get("name")))
