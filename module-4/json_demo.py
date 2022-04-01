import json

mydict = {
    'people': [
        {
            'name': 'hareesh',
            'age': 22,
            'id': 1
        },
        {
            'name': 'Sidharth',
            'age': 23,
            'id': 2
        },
        {
            'name': 'raghu',
            'age': 26,
            'id': 3
        }
    ]
}
json_string = json.dumps(mydict, indent=4)
with open('mydata.json', 'w') as f:
    f.write(json_string)
