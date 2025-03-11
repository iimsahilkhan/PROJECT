import requests
import json


city = input("Enter the name of the city\n")

url = f"http://api.weatherapi.com/v1/current.json?key=9fa6955d9c7e433bb7a81707251103&q={city}"

r = requests.get(url)
print(r.text)
widc = json.loads(r.text)
print(widc["current"]["temp_c"])