#!/usr/bin/python3
"""A script that:
- takes in a URL,
- sends a request to the URL
"""
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    r = urllib.request.Request(url)
    with urllib.request.urlopen(r) as res:
        print(dict(res.headers).get("X-Request-Id"))
