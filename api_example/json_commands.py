import json

data_as_string = '{"ID":"123" "Name": "John"}'

data_as_json = json.loads(data_as_string)
print (data_as_json["Name"])

print ("Test End")

