#!/usr/bin/python3

"""
function that queries the Reddit API and prints the titles of t
he first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    prints first 10 hot posts for given subreddit
    """

    if subreddit is None or type(subreddit) is not str:
        print("None")

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'deeIsProbing'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print("None")
        return

    data = response.json()['data']['children']
    for post in data[:10]:
        print(post['data']['title'])
