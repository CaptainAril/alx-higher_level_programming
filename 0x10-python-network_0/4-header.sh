#!/bin/bash
# Sends a `GET` request to a URL with a header varaible and displays the response
curl -sH "X-School-User-Id: 98" "$1"
