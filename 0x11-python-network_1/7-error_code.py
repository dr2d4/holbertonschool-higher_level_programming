#!/usr/bin/python3
"""
    Manage exceptions in http request
"""
import requests
import sys


def errorcode():
    """
        Manage KeyError exception
    """
    resp = requests.get(sys.argv[1])

    try:
        if resp.status_code > 400:
            print("Error code: {}".format(resp.status_code))
        else:
            print(resp.content.decode("utf-8"))
    except KeyError:
        pass


if __name__ == "__main__":
    errorcode()
