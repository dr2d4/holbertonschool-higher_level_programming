#!/bin/bash
# Dysplays status code
curl $1 -sI -w '%{http_code}' -o /dev/null
