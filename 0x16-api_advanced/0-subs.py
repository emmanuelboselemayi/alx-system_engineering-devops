#!/usr/bin/python3
"""Module for querying the Reddit API"""

import requests

def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers to the subreddit.
    
    Args:
        subreddit (str): The name of the subreddit.
        
    Returns:
        int: The number of subscribers, or 0 if the subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "My-User-Agent"}
    
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code != 200:
        return 0
    
    try:
        data = response.json().get("data", {})
        return data.get("subscribers", 0)
    except ValueError:
        return 0

# Example usage:
if __name__ == "__main__":
    subreddit_name = "python"
    print(f"The subreddit '{subreddit_name}' has {number_of_subscribers(subreddit_name)} subscribers.")

