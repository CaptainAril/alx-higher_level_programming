#!/usr/bin/python3
"""Sends a `POST` requests with a letter as parameter"""


if __name__ == '__main__':
    import requests
    from sys import argv
    letter = "" if len(argv) == 1 else argv[1]
    payload = {'q': letter}
    r = requests.post('http://0.0.0.0:5000/search_user', data=payload)
    try:
        j = r.json()
        if len(j) == 0:
            print("No result")
        else:
            print("[{}] {}".format(j.get('id'), j.get('name')))
    except Exception:
        print("Not a valid JSON")
