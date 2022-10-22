#!/usr/bin/python3
"""Sends a request to a URL and displays the body of the response
or status code if error."""


if __name__ == '__main__':
    from sys import argv
    import requests

    try:
        r = requests.get(argv[1])
        # print(r.text)
    except requests.exceptions.ConnectionError as e:
        print(e)
        # print(r.status_code)
