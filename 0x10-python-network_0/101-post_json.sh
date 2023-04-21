#!/usr/bin/bash
# Post a JSON data to URL
curl -sX POST -d "@$2" -H "Content-Type: application/json" "$1"
