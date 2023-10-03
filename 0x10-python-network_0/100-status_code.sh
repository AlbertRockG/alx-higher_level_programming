#!/bin/bash
# Sends a request to a URL and displays only the status code of response.
curl -sL "$1" | head -1 | cut -d ' ' -f2
