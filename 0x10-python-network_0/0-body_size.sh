#!/bin/bash
# Displays size of the download file
curl -w '%{size_download}\n' -s $1
