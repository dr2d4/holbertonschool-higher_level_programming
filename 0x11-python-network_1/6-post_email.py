#!/usr/bin/python3
"""
    Send post from requests
"""
import requests
import sys


def post():
    """
        Send post
    """
    result = requests.post(sys.argv[1], data={"email": sys.argv[2]})
    print(result.text)


if __name__ == "__main__":
    post()
