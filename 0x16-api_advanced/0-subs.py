#!/usr/bin/python3
""" Exporting csv files"""
import json
import requests
import sys


def number_of_subscribers(subreddit):
    """Read reddit API and return number subscribers"""
    headers = {'user-agent': 'Mozilla/5.0'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    client = requests.session()
    client.headers = headers
    r = client.get(url, allow_redirects=False)
    if r.status_code == 200:
        return 'OK'
    else:
        return ''


# Example usage:
if __name__ == "__main__":
    subreddit = sys.argv[1]
    print(number_of_subscribers(subreddit))

