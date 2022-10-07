import json

with open('data.json') as json_data:
    data = json.load(json_data)
    destinations = data['destinations']
