#!/bin/bash
# Takes a URL, sends POST request and displays the body of the response
curl -sX POST -F email=test@gmail.com -F subject="I will always be here for PLD" "$1"
