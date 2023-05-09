#!/usr/bin/python3
""" prints the titles of the first 10 hot posts listed for a given subreddit"""
import requests


def top_ten(subreddit):
    '''Prints titles of top 10 hot posts for subreddit'''
    URL = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    USERAGENT = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 \
        Safari/537.36'}
    req = requests.get(URL, headers=USERAGENT)
    if req.status_code is not 200:
        print(None)
        return
    jreq = req.json()
    data_path = jreq['data']['children']
    for i in range(10):
        print(data_path[i]['data']['title'])
