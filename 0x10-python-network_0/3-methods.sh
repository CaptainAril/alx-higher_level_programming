#!/bin/bash
# Lists all HTTP methods allowed by the server
curl -sIX OPTIONS "$1" | grep 'Allow' | cut -d " " -f 2-
