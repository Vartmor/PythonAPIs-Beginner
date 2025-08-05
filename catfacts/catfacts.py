import requests

url = "https://catfact.ninja/fact"
response = requests.get(url)

data = response.json()

print(f"Here is the fact of the day: {data['fact']}")
