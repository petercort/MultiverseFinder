#! /usr/bin/python
import json

print "Enter a card name",
cardMatch = raw_input()

json_file='AllSets.json'
json_data=open(json_file)
data=json.load(json_data)
json_data.close()

sets = []

for val in data:
	setCode=(data[val]["code"])
	sets.append(str(setCode))

for val in sets:
	cardNumber=0
	x=0
	numCards=len(data[val]["cards"])
	while cardNumber < numCards:
		cardName=data[val]["cards"][x]["name"]
		if cardName==cardMatch:
			print("Card Name Matched")
			print("http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid="+str(data[val]["cards"][x]["multiverseid"]))
			quit()
		cardNumber=cardNumber+1
		x=x+1