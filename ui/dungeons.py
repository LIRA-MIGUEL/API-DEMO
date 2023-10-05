import requests 
import json

URI = "https://www.dnd5eapi.co/api/classes"

response = requests.get(URI)

print(f"GET: {response.text}")

response_json = json.loads(response.text)

for i in range[12]:

data = response_json['results'][i]
name = data['name']
print(f"data: {i + 1}: {name}")
