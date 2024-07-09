#!/usr/bin/python3
"""
-takes in a URL, sends a request to the URL and
-displays the body of the response
"""
import requests
import sys

if __name__ == '__main__':

    url = sys.argv[1]
    reply = requests.get(url)
    status = eval(f"reply.status_code")
    if status >= 400:
        print("Error code:", status)
    else:
        print(reply.text)
