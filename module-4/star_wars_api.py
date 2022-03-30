import requests,json
data = requests.get('http://swapi.dev/api/people').json()
json_object = json.dumps(data,indent=6)
with open('star_wars_data.txt', 'w') as f:
    f.write(json_object)