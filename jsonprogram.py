import json

# load data from json file, and convert it to a list
#json_data = json.loads(open("guest_card.json").read())
with open('guest_card.json','r') as j:
	data = j.read()
	d = json.loads(data)
	print(d)
	 	


