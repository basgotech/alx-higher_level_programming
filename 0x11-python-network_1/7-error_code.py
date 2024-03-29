#!/usr/bin/python3
"""
A script to fetch the content of a given URL using requests library.
"""
import sys
import requests


if __name__ == "__main__":
    url_grapper = sys.argv[1]
    """ hecking the status code of the response """
    req = requests.get(url_grapper)
    if req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)
