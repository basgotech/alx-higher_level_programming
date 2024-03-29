#!/usr/bin/python3
"""
- A script to fetch the value of the "X-Request-Id"
- header from a specified URL using urllib.
"""
import sys
import urllib.request

if __name__ == "__main__":
    url_grapper = sys.argv[1]

    res = urllib.request.Request(url_grapper)
    with urllib.request.urlopen(res) as resq:
        print(dict(resq.headers).get("X-Request-Id"))
