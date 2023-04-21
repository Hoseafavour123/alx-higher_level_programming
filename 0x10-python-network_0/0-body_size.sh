#!/usr/bin/bash
# Display the size of HTTP response message
curl -sI "$1" | grep "Content-Length" | cut -d " " -f2
