#!/usr/bin/env python

# get a page the hard way

import urllib3

http = urllib3.PoolManager()

r = http.request("GET", "https://www.disney.com")
print(r.data)

