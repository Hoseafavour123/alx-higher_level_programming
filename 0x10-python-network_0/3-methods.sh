#!/bin/bash
# Display supported HTTPS methods
curl -sI | grep "Allow" | cut -d " " -f2-
