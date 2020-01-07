#!/bin/bash
# Call GET method and add extra header
curl $1 -sX GET -H "X-HolbertonSchool-User-Id: 98"
