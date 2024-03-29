#!/usr/bin/python3
"""This module fetches a url using the python's `urllib` package."""


if __name__ == '__main__':
    import urllib.request

    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as p:
        body = p.read()

    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
    print("\t- utf8 content: {}".format(body.decode("UTF-8")))
