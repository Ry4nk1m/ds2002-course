#!/usr/bin/env python3
import os
import json
import requests

GHUSER = os.getenv('GITHUB_USER')
url = f'https://api.github.com/users/{GHUSER}/events'
print(f"Fetching data from: {url}")
r = json.loads(requests.get(url).text)
print(f"--- Recent Activity for {GHUSER} ---")
for x in r[:5]:
    # Combine event type and repo name
    event = x['type'] + ' :: ' + x['repo']['name']
    print(event)
