#!/usr/bin/python3
"""
sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import sys
import requests

if __name__ == "__main__":
    """Checking if the script is run as the main program"""
    
    let = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": let}

    req = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        res = req.json()
        if res == {}:
            print("No result")
        else:
            print("[{}] {}".format(res.get("id"), res.get("name")))
    except ValueError:
        print("Not a valid JSON")
