#!/usr/bin/python3
"""This module fetches a url using the python's `urllib` package."""


if __name__ == '__main__':
    import urllib.request
    import urllib.error
    from sys import argv

    try:
        with urllib.request.urlopen(argv[1]) as p:
            body = p.read()
            body = body.decode("UTF-8")
            print(body)
    except urllib.error.HTTPError as e:
        print(e.code)
