#!/usr/bin/python3
"""
    Get json from url
"""
import requests
import sys


def searchapi():
    """
        Send post request
    """

    q = sys.argv[1] if len(sys.argv) > 1 else ""

    resp = requests.post("http://0.0.0.0:5000/search_user", data={"q": q})

    try:
        data = resp.json()

        if data:
            print("[{}] {}".format(data["id"], data["name"]))
        else:
            print("No result")
    except:
        print("Not a valid JSON")


if __name__ == "__main__":
    searchapi()
