#!/bin/bash

# Check if a URL is provided as argument
curl -s "$1" | wc -c
