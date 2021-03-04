import requests
import json

url = "https://geocode-maps.yandex.ru/1.x"
coords = "37.637937 55.812368"
params = {
    "geocode": coords,
    "apikey": "6d96e1bf-ea8f-47f8-b77b-cfff232ea793",
    "format": "json"
}
response = requests.get(url, params=params)
response = json.loads(response.text)
# print(response)


with open('lesson-1_task-2.json', 'w') as write_file:
    json.dump(response, write_file)