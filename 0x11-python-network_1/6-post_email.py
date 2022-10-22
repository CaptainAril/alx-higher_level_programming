#!/usr/bin/pyhton3
"""Sends a `POST` request to a URL and displays the body."""


if __name__ == '__main__':
    from sys import argv
    import requests

    param = {'email': argv[2]}
    r = requests.post(argv[2], data=param)
    print(r.text)
