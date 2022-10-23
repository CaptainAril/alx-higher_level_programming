#!/usr/bin/python3
"""This script lists 10 commits from a github repository
 - takes in two arguments (repository name and owner name)
"""

if __name__ == '__main__':
    import requests
    from sys import argv

    url = 'https://api.github.com/repos/{}/{}/commits'\
        .format(argv[1], argv[2])
    r = requests.get(url)
    print(r.headers)
    commits = r.json()
    print(commits)
    try:
        for i in range(10):
            commit = commits[i]
            sha = commit.get('sha')
            author_name = commit.get("commit").get('author').get('name')
            print("[{}] {}".format(sha, author_name))
    except IndexError:
        pass
