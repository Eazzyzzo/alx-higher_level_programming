#!/usr/bin/python3
"""This script
- takes in a URL and an email address
- sends a POST request to the passed URL with the email as a parameter
- displays the body of the response.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    reply = requests.post(url, data=value)
    print(reply.text)
