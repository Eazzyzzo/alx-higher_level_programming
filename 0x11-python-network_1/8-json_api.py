#!/usr/bin/python3
"""A script tha:
- takes in a letter
- sends POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
import sys
import requests


if __name__ == "__main__":
    note = "" if len(sys.argv) == 1 else sys.argv[1]
    load = {"q": note}

    p = requests.post("http://0.0.0.0:5000/search_user", data=load)
    try:
        reply = p.json()
        if reply == {}:
            print("No result")
        else:
            print("[{}] {}".format(reply.get("id"), reply.get("name")))
    except ValueError:
        print("Not a valid JSON")
