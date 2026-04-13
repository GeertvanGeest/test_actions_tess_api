#!/usr/bin/env python3
import requests
import sys

url = "https://tess.elixir-europe.org/materials"
headers = {"Accept": "application/vnd.api+json"}
response = requests.get(url, headers=headers)
print(f"Status: {response.status_code}")

try:
    data = response.json()
    print("Successfully parsed JSON")
except requests.exceptions.JSONDecodeError as e:
    print(f"Error: Failed to parse JSON - {e}")
    print(f"Response: {response.text[:200]}")
    sys.exit(1)
