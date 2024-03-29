#!/usr/bin/python3
"""This script lists 10 commits from a github repository
 - takes in two arguments (repository name and owner name)
"""

if __name__ == '__main__':
    import requests
    from sys import argv

    url = 'https://api.github.com/repos/{}/{}/commits'\
        .format(argv[2], argv[1])
    r = requests.get(url)
    commits = r.json()
    try:
        for i in range(10):
            commit = commits[i]
            sha = commit.get('sha')
            author_name = commit.get("commit").get('author').get('name')
            print("{}: {}".format(sha, author_name))
    except IndexError:
        pass
