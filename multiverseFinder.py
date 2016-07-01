#! /usr/bin/python
import json

#print "Enter a card name:",
#cardMatch = raw_input()

cardNames = []
cardInt = 0
print "Enter path of list:",
listDirectory = raw_input()
f=open(listDirectory)
data=f.read().splitlines()
for line in data:
	cardNames.append(line)
f.close()

json_file='AllSets.json'
json_data=open(json_file)
data=json.load(json_data)
json_data.close()

sets = []

for val in data:
	setCode=(data[val]["code"])
	sets.append(str(setCode))

while cardInt < len(cardNames):
	cardName = cardNames[cardInt]
	for val in sets:
		cardNumber=0
		x=0
		y=0
		numCards=len(data[val]["cards"])
		while cardNumber < numCards:
			cardMatch=data[val]["cards"][x]["name"]
			if cardName==cardMatch:
				print("Card Name Matched")
				print("http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid="+str(data[val]["cards"][x]["multiverseid"]))
			cardNumber=cardNumber+1
			x=x+1
			break
		break
cardInt = cardInt+1