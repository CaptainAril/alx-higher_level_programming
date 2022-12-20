#!/bin/bash
# sends a request to a URL passed as argument, and displays only the stattly the status code of the resoponse.
curl $1 -s -o /dev/null -w "%{http_code}"
