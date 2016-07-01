#! /usr/bin/python
import json

#print "Enter a card name:",
#card = raw_input()

cardNames = []
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

##Setting the sets list
sets = []

for val in data:
	setCode=(data[val]["code"])
	sets.append(str(setCode))
##

def returnName( cardName ):
	for val in sets:
		default = 'no value'
		cardNumber=0
		x=0
		numCards=len(data[val]["cards"])
		while cardNumber < numCards:
			cardMatch=data[val]["cards"][x]["name"]
			if cardName == cardMatch:
				if "multiverseid" in data[val]["cards"][x]:
					print("Card Name Matched")
					print("http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid="+str(data[val]["cards"][x]["multiverseid"]))
					return
			cardNumber=cardNumber+1
			x=x+1
 
#print(card)
#returnName(card)

for val in cardNames:
	print(val)
	returnName(val)
