#!/bin/bash
# Sends a request to a given URL and displays all HTTP methods the server will accept.
curl -sI "$1" | awk -F ': ' '/^Allow/ {print $2}'
