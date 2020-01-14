#!/usr/bin/python3
"""
    Call to api
"""
import requests
import sys


def searchapi():
    """
        Get list people
    """
    seach = {"search": sys.argv[1]}
    result = requests.get("https://swapi.co/api/people", params=search)

    try:
        data = result.json()

        print("Number of results: {}".format(data["count"]))

        for x in data["results"]:
            print(x["name"])
    except:
        print("Not a valid JSON")


if __name__ == "__main__":
    searchapi()
