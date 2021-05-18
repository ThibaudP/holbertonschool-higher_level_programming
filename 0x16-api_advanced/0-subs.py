#!/usr/bin/python3
"""
0-subs
"""
import requests
import json


def number_of_subscribers(subreddit):
    """fetches the number of subscribers to a subreddit"""

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "ubuntu:hbtn:v1.0 (by /u/eskaps)"}

    # print("{}".format(url))

    request = requests.get(url, headers=headers, allow_redirects=False)

    # print(request.json().get("data"))
    # print(json.dumps(json.loads(request.text).get("data"), indent=2))

    if request.status_code == 200:
        return request.json().get("data").get("subscribers")

    return 0
