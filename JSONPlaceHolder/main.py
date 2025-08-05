import json

import requests

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
veri = response.json()

with open("posts.json", "w", encoding="utf-8") as f:

    json.dump(veri,f, indent=4)




