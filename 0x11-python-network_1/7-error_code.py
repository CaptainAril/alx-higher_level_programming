#!/usr/bin/python3
"""Sends a request to a URL and displays the body of the response
or status code if error."""


if __name__ == '__main__':
    from sys import argv
    import requests

    r = requests.get(argv[1])
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
