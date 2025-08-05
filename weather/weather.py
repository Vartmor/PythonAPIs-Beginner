import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()

api_key = os.getenv("WEATHER_API_KEY")
city = input("Hava Durumu Uygulamasina Hos Geldiniz.\nSehir giriniz ---> ")
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=tr"


response = requests.get(url)

if response.status_code == 200:

    data = response.json()

    file = "hava.json"
    with open(file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    #print(data.keys())

    print(f"{data['name']} için hava durumu: {data['weather'][0]['description']}")
    print(f"Sıcaklık: {data['main']['temp']}°C")
    print(f"Nem: {data['main']['humidity']}%")
    print(f"Rüzgar: {data['wind']['speed']} m/s")
    print(f"Min: {data['main']['temp_min']}°C | Max: {data['main']['temp_max']}°C")

elif response.status_code == 404:
    print("Şehir bulunamadı. Lütfen doğru bir şehir ismi girin.")

else:
    print("Hava durumu alınamadı:", response.status_code)
