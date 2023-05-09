#!/usr/bin/python3
"""returns the number of subscribers (not active users, total subscribers)"""
import requests


def number_of_subscribers(subreddit):
    """Function that returns total subscriber number"""
    URL = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    USERAGENT = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 \
        Safari/537.36'}
    req = requests.get(URL, headers=USERAGENT)
    if req.status_code != 200:
        return (0)
    jreq = req.json()
    return (jreq['data']['subscribers'])
