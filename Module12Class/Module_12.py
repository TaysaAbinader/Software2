#Consuming an API
import requests
import json


#TV shows example:
keyword = input("Give a keyword: ")
request = "https://api.tvmaze.com/search/shows?q=" + keyword
response = requests.get(request).json()
#print(response)
#print(json.dumps(response, indent = 3))

try:
    response = requests.get(request)
    if response.status_code == 200:
        json_response = response.json()
        for a in json_response:
            print(a["show"])
            print(a["show"]["name"])

except requests.exceptions.RequestException as example:
    print("Request could not be completed", example)

#for avai_show in response:
    #print(avai_show["show"] ["name"])




"""
response = requests.get("https://api.stackexchange.com/2.2/questions?order=desc&sort=activity&site=stackoverflow")

for data in response.json()['items']:
    print(data['title'])
    print(data['link'])
"""