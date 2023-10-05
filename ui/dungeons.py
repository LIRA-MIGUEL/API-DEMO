import requests 
import json

URI = "https://www.dnd5eapi.co/api/classes"

response = requests.get(URI)

print(f"GET: {response.text}")

response_json = json.loads(response.text)

for ¡ in range[12]:

print(response_json{}")
