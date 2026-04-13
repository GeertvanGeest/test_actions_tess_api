#!/usr/bin/env python3
import requests

url = "https://tess.elixir-europe.org/materials"
response = requests.get(url)
print(f"Status: {response.status_code}")
print(f"Response: {response.text[:200]}")
