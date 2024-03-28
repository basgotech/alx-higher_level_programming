#!/bin/bash
# This script sends a GET request to the URL-
# passed as the first argument using curl
curl -s -o /dev/null -w "%{http_code}" "$1"
