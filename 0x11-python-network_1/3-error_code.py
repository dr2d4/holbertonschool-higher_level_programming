#!/usr/bin/python3
"""
    Manage errors in http request
"""
from urllib.request import urlopen
from urllib.error import HTTPError
import sys


def sender():
    """
        Manage HTTPError exception
    """
    try:
        with urlopen(sys.argv[1]) as resp:
            print(resp.read().decode("utf-8"))
    except HTTPError as e:
        print("Error code: {}".format(e.code))


if __name__ == "__main__":
    sender()
