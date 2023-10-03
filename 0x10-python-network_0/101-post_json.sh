#!/bin/bash
# Takes a URL, sends a JSON POST request and displays the body of the response
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
