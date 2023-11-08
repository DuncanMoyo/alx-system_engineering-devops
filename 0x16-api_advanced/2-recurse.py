#!/usr/bin/python3
"""
function that queries the Reddit API, parses the title of all hot articles,
and prints a sorted count of given keywords (case-insensitive,
delimited by spaces. Javascript should count as javascript,
but java should not).
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    returns list of hot posts.
    """
    if subreddit is None or type(subreddit) is not str:
        return None

    headers = {
        'User-Agent': 'deeIsProbing'
        }

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    if after:
        url += "?after={}".format(after)

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json()['data']
    hot_list += [post['data']['title'] for post in data['children']]

    if data['after']:
        return recurse(subreddit, hot_list, data['after'])

    return hot_list
