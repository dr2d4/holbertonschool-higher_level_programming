#!/usr/bin/python3
"""
    Call Api GitHub
"""
import requests
from requests.auth import HTTPBasicAuth
import sys


def call_gh_api():
    """
        Get Id GitHub
    """
    auth = (HTTPBasicAuth(sys.argv[1], sys.argv[2]))

    result = requests.get("https://api.github.com/user", auth=auth)

    try:
        print(result.json()["id"])
    except:
        print("None")


if __name__ == "__main__":
    call_gh_api()
