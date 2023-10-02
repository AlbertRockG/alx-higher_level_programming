#!/bin/bash
# Takes a URL, sends a GET and displays the body response
curl -sL -H "X-School-User-Id: 98" "$1"
