#!/bin/bash
# The script takes in a URL, sends a request to it, and displays the size of the body of the
curl -s "$1" | wc -c
