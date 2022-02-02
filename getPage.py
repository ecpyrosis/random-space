#!/usr/bin/env python3

# grab first page of a website
# suddenly easier thanks to https://docs.python-requests.org/en/master/

# import urllib3
# http = urllib3.PoolManager()
# r = http.request("GET", "https://www.disney.com")
# print(r.data)

import requests

r = requests.get('https://www.disney.com')
print(r.content)
# print(r.text)
# print(r.headers)
# print(r.elapsed)