#!/usr/bin/python3
# send request to url
import urllib.request
import sys

# Extract the URL from command line argument
url = sys.argv[1]

# Send request to the URL and retrieve the response headers
with urllib.request.urlopen(url) as response:
    request_id = response.headers.get('X-Request-Id')
    print(request_id)
