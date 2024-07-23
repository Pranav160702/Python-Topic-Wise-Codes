json_str ='''
{
    "name": "Eric Smith",
    "age": 32,
    "phoneNumbers": [
        {
            "type": "home",
            "number": "(212) 555-3276"
        },
        {
            "type": "work",
            "number": "(332) 555-1234"
        }
    ],
    "spouse": null,
    "children": [],
    "employed": true
}
'''

import json

eric = json.loads(json_str)
# print(eric)

print(json.dumps(eric, indent = 2))


