#!/usr/bin/python3
"""
returns the number of subscribers (not active users, total subscribers)
for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    returns number of subs for the given subreddit.
    """
    
    if subreddit is None or type(subreddit) is not str:
        return 0

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'deeIsProbing'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0
    return response.json()['data']['subscribers']
