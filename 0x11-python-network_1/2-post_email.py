#!/usr/bin/python3
"""A script that:
- takes in a URL
- sends a POST request to the passed URL
"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url_grapper = sys.argv[1]
    value_grapper = {"email": sys.argv[2]}
    sto = urllib.parse.urlencode(value_grapper).encode("ascii")

    getter = urllib.request.Request(url_grapper, sto)
    with urllib.request.urlopen(getter) as res:
        print(res.read().decode("utf-8"))
