#!/usr/bin/python3
"""recursive function that queries the Reddit API"""
import requests


def recurse(subreddit, hot_list=[], count=0, after_val=None):
    '''returns list of titles for hot articles'''
    URL = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    USERAGENT = {'User-Agent': 'User-Agent': 'Mozilla/5.0 (Windowsi\
         NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
        Chrome/58.0.3029.110 Safari/537.36'}
    params = {'limit': 100}
    if count > 0:
        params['after'] = after_val
    req = requests.get(URL,
                       headers=USERAGENT,
                       params=params)
    if req.status_code is not 200:
        return (None)
    jreq = req.json()
    data_path = jreq['data']['children']
    for i in range(len(data_path)):
        hot_list.append(data_path[i]['data']['title'])
    count += 1
    after_val = jreq['data']['after']
    if after_val is None:
        return (hot_list)
    else:
        return (recurse(subreddit, hot_list, count, after_val))
