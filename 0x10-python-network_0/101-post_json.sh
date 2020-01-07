#!/bin/bash
# Send json by POST method
curl $1 -sX POST -H "Content-Type: application/json" -d @$2
