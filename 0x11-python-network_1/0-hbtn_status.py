#!/usr/bin/python3
import urllib.request
# URL to fetch
url = 'https://alx-intranet.hbtn.io/status'

# Open URL and fetch response using urllib
with urllib.request.urlopen(url) as response:
    # Read the response body
    body = response.read()
    
    # Print the body response with relevant information
    print("Body response:")
    print("\t- type:", type(body))
    print("\t- content:", body)
    print("\t- utf8 content:", body.decode('utf-8'))
