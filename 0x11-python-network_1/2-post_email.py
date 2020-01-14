#!/usr/bin/python3
"""
    Send post from urllib
"""
from urllib.request import urlopen, Request
from urllib import parse
import sys


def sender():
    """
        Send post
    """
    data = {"email": sys.argv[2]}

    data = parse.urlencode(data)
    data = data.encode("ascii")

    req = Request(sys.argv[1], data)

    with urlopen(req) as resp:
        print(resp.read().decode("utf-8"))


if __name__ == "__main__":
    sender()
