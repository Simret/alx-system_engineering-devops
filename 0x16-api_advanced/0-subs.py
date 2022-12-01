#!/usr/bin/python3
"""API"""
import requests


def number_of_subscribers(subreddit):
    """
    a function that queries the Reddit API
    and returns the number of subscribers
    """

    data = requests.get("https://www.reddit.com/r/{}/about.json"
                        .format(subreddit),
                        headers={"User-Agent": "My-User-Agent"},
                        allow_redirects=False)
    if data.status_code >= 300:
        return 0
    data_dict = data.json()
    return data_dict["data"]["subscribers"]