#!/usr/bin/env python3

# grab first page of a website

import requests

r = requests.get('https://www.disney.com')
print(r.content)