#!/usr/bin/python3
""" takes in a URL and an email
    -sends a POST request to the passed URL
    -with the email as a parameter, and displays 
    -the body of the response (decoded in utf-8)
"""
import sys
import urllib.request


if __name__ == '__main__':
    """Makes a post request"""
    url = sys.argv[1]
    data = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(data).encode('ascii')
    request = urllib.request.Request
    with urllib.request.urlopen(request(url, data)) as reply:
        print(reply.read().decode('utf-8'))
