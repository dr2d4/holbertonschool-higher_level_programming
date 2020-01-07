#!/bin/bash
# Displays size of the download file
curl -sI "$1" | grep "Content-Length" | cut -d' ' -f 2
