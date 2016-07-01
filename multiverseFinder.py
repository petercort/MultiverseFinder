#! /usr/bin/python
import json

#print "Enter a card name:",
#card = raw_input()

cardNames = []
numEntered = []
#print "Enter path of list:",
#listDirectory = raw_input()
listDirectory=('cardlist.txt')
f=open(listDirectory)
data=f.read().splitlines()

for i in range(0,len(data)):
	string=data[i].split(" ", 1)
	##add the name to list
	cardNames.append(string[1])
	numEntered.append(string[0])
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
					output = "http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid="+str(data[val]["cards"][x]["multiverseid"])
					return(output)
			cardNumber=cardNumber+1
			x=x+1
 
#print(card)
#returnName(card)

htmlHeader = '<!DOCTYPE html><html lang="en-US"><head><title>HTML DOM Document Objects</title><meta charset="utf-8"><link rel="icon" href="/favicon.ico" type="image/x-icon"></head><body>'
htmlFooter = '</body><footer></footer></html>'

print(htmlHeader)
print("<br />")
for i in range(0, len(cardNames)):
	gathererOutput = returnName(cardNames[i])
	print("<a href='"+gathererOutput+"'>"+numEntered[i] + " " + cardNames[i] + "</a>" )
	print("<br />")

#for val in cardNames:
#	output = returnName(val)
#	print("<a href='"+output+"'>"+val+"</a>")
#	
print("<br />")	
print(htmlFooter)