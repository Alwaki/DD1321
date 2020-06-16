#Course: DD1321 2019
#Student: Alexander Wallén Kiessling
#Project: Lab A

#Import packages
from Alexander import *

#Create instance of class MapEdges.
c = MapEdges()

#Utilize neighbors attribute
islandList = c.neighbors

#If two entries have matching (complete or partial) neighbours, they
#must be on the same island. As such,remove any such entry in list.
for x in islandList:
    templist = islandList.copy()
    templist.remove(x)
    for y in templist:
        matches = set(x).intersection(y)
        if not not matches: #double not due to empty set boolean notation
            islandList.remove(y)

#Print resultant number
print(len(islandList))
