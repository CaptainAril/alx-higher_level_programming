#!/usr/bin/python3
"""Sends a `POST` requests with a letter as parameter"""


if __name__ == '__main__':
    import requests
    from sys import argv
    try:
        q = argv[1]
    except IndexError:
        q = ""
    payload = {'q': q}
    r = requests.post('http://0.0.0.0:5000/search_user', data=payload)
    try:
        j = r.json()
        if len(j) == 0:
            print("No result")
        else:
            print("[{}] {}".format(j['id'], j['name']))
    except requests.exceptions.InvalidJSONError:
        print("Not a valid JSON")
