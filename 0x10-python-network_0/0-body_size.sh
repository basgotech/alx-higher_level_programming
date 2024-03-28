#!/bin/bash
# Get the byte size of the HTTP.
curl -s "$1" | wc -c
