#!/usr/bin/python3
"""API"""
import requests


def top_ten(subreddit):
    """
     a function that queries the Reddit API and prints the titles
     of the first 10 hot posts listed for a given subreddit
     subreddit : name of fild
    """
    data = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10"
                        .format(subreddit),
                        headers={"User-Agent": "My-User-Agent"},
                        allow_redirects=False)
    if data.status_code >= 300:
        print('None')

    else:
        data_dict = data.json()
        for child in data_dict.get("data").get("children"):
            print(child.get("data").get("title"))
