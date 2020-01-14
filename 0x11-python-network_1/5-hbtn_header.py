#!/usr/bin/python3
"""
    Reader header from request response
"""
import requests
import sys


def header():
    """
        Displays specific header
    """
    resp = requests.get(sys.argv[1])

    print(resp.headers.get("X-Request-Id", None))


if __name__ == "__main__":
    header()
