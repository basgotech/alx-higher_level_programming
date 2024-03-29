#!/usr/bin/python3
"""
A Python script to retrieve the 10 most recent commits
"""

import requests
import sys

if __name__ == "__main__":
    repos_name = sys.argv[1]
    owner_name = sys.argv[2]

    url_grapper = f"https://api.github.com/repos/{owner_name}/{repos_name}/commits"
    params_grapepr = {'per_page': 10}
    res = requests.get(url_grapper, params=params_grapepr)

    if res.status_code == 200:
        commits_holder = res.json()
        for commit in commits_holder:
            sha_hol = commit['sha']
            owner = commit['commit']['author']['name']
            print(f"{sha_hol}: {owner}")
    else:
        print("Error:", res.status_code)
