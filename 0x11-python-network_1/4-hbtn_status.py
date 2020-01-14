#!/usr/bin/python3
"""
    Get info from url with requests
"""
import requests


def status():
    """
        Displays info of the request response
    """
    resp = requests.get("https://intranet.hbtn.io/status")

    print("Body response:")
    print("\t- type: {}".format(type(resp.text)))
    print("\t- content: {}".format(resp.text))


if __name__ == "__main__":
    status()
