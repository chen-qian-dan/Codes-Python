import json

people_string = ''' 
{
  "people": [
     {
       "name": "Qian Chen", 
       "phone": "0404-123-345",
       "email": ["chen.qian.dan@gmail.com", "chen.qian.dan@icloud.com"],
       "has_license": false
     },  
     {
       "name": "Dan Chen", 
       "phone": "0101-123-345",
       "email": null,
       "has_license": true
     }
  ]
}
'''
# string to dict
data = json.loads(people_string)

# data is dict
# 'people' is key
# value of the key is list of dict
for person in data['people']:
    print(person)
    print(person['name'])

# delete phone key and convert back to json
for person in data['people']:
    del person['phone']

# dict to json object
new_string = json.dumps(data)
print(new_string)

# make it easier to read.
# indent constrols 缩格
new_string = json.dumps(data, indent=2)

# will sort all level of keys.
new_string = json.dumps(data, indent=2, sort_keys=True)
print(new_string)


