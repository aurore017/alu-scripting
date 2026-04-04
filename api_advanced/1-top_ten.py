#!/usr/bin/python3
"""
Fetch and print the top 10 hot post titles from a subreddit
"""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts of a subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "python:top_ten:v1.0 (by /u/anonymous)"}
    params = {"limit": 10}

    try:
        response = requests.get(url, headers=headers,
                                params=params, allow_redirects=False)

        if response.status_code != 200:
            print("None")
            return

        data = response.json().get("data", {}).get("children", [])

        for post in data:
            print(post.get("data", {}).get("title"))

    except Exception:
        print("None")
