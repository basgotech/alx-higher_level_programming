#!/bin/bash

# Check if a URL is provided as argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Get the URL from command line argument
URL=$1

# Send a request to the URL and store the size of the response body in bytes
RESPONSE_SIZE=$(curl -s -o /dev/null -w "%{size_download}" $URL)

# Display the size of the response body in bytes
echo "$RESPONSE_SIZE"
