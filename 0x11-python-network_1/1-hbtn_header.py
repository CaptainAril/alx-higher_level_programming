#!/usr/bin/python3
"""Sends request to a URL and displays the value of `X-Request-Id` header """

if __name__ == '__main__':
    from sys import argv
    import urllib.request

    with urllib.request.urlopen(argv[1]) as r:
        headers = r.headers
    print(headers.get("X-Request-Id"))
