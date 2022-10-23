#!/usr/bin/python3
"""This scipt takes in GitHub credentials (username and password),
using the GitHub API displays user id."""


if __name__ == '__main__':
    import requests
    from sys import argv

    Header = {
        'Accept': 'application/vnd.github+json',
        'Authorization': 'Bearer {}'.format(argv[2])
    }
    URL = 'https://api.github.com/user'
    r = requests.get(URL, headers=Header)
    try:
        JSON = r.json()
        print(JSON.get('id'))
    except Exception:
        print("No Valid JSON")
