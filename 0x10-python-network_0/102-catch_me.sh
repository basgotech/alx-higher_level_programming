#!/bin/bash
# Make a POST request to 0.0.0.0:5000/catch_me with custom header
curl -s -X PUT 0.0.0.0:5000/catch_me -d "user_id=98" -H "Origin: ALXSchool" -L -o /dev/null -w "You got me!"
