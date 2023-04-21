#!/bin/bash
# Display supported HTTPS methods
curl -sI "$1" | grep "Allow" | cut -d " " -f2-
