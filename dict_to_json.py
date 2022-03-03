import json

mydict = {
    "people": [
        {
            "name": "Bob",
            "age": 11,
            "nationality": "English"
        },
        {
            "name": "Boris",
            "age": 11,
            "nationality": "Russian"
        },
        {
            "name": "Lisa",
            "age": 11,
            "nationality": "Spanish"
        }
    ]
}

json_string = json.dumps(mydict, indent=2)
with open('mydata.json', 'w') as f:
    f.write(json_string)

