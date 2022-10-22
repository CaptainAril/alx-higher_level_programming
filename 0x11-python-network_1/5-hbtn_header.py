#!/usr/bin/python3
"""Fetches a URL using `requests` package
and displays a specified header value."""


if __name__ == '__main__':
    import requests
    from sys import argv

    r = requests.get(argv[1])
    headers = r.headers
    print(headers.get("X-Request-Id"))
