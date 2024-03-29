#!/usr/bin/python3
"""
This script retrieves the user ID from the GitHub API using basic authentication.
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    sec_proced = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    req = requests.get("https://api.github.com/user", auth=sec_proced)
    print(req.json().get("id"))
