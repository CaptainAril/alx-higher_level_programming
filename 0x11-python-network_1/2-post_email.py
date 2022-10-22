#!/usr/bin/python3
"""Sends a `POST` request to a URL and displays the body."""


if __name__ == '__main__':
    from sys import argv
    import urllib.request

    value = {'email': argv[2]}
    en_value = urllib.parse.urlencode(value)
    val = en_value.encode("UTF-8")
    request = urllib.request.Request(argv[1], data=val, method='POST')
    with urllib.request.urlopen(request) as r:
        body = r.open()
    print(body.decode("UTF-8"))
