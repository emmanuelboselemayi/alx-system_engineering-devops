#!/usr/bin/python3
""" 
Queries the Reddit API and returns the  number of subcribers 
"""

import requests
    
    def number_of_subcribers(subreddit):
        """Queries the Reddit API and returns the number of subcribers
        to the subbreddit"""

        sub_info = requests.get("https://www.reddit.com/r/{}/about.json"
                                .format(subreddit),
                                headers={"User-Agent": "My-User-Agent"},
                                allow_redirects=False)

    if sub_info.status_code >= 300:
            return 0

        return sub_info.json().get("data").get("subscribers")


