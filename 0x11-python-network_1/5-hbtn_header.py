#!/usr/bin/python3
"""
- A script to fetch the value of the "X-Request-Id"
- header from a specified URL.
"""
import sys
import requests

if __name__ == "__main__":
    url_grapper = sys.argv[1]
    res = requests.get(url_grapper)
    print(res.headers.get("X-Request-Id"))
