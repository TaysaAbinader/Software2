import requests
import json

api_key = "key removed per teacher request"
city = input("Choose a city: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

try:
    response = requests.get(url)
    if response.status_code == 200:
        reply = response.json()
        #print(json.dumps(reply, indent=2))
        name = reply['name']
        print(name)
        for weather in reply['weather']:
            description = weather['description']
            print(description)
        temperature = reply['main']['temp']
        print(temperature)

except requests.exceptions.RequestException as e:
    print("Not able to attend request.")

