#!/usr/bin/python3
"""
    Reader header from request response
"""
from urllib.request import urlopen
import sys


def fetcher():
    """
        Displays specific header
    """
    with urlopen(sys.argv[1]) as resp:
        print(resp.info()["X-Request-Id"])


if __name__ == "__main__":
    fetcher()
