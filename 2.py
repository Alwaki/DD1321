#Course: DD1321 2019
#Student: Alexander Wallén Kiessling
#Project: Lab A

#Import packages
from Alexander import *
from karta import *

#create instance
c = MapEdges()

#create row list from map
rows = island_map.split("\n")

#iterate over map in y and x directions (y iterates downward, as specified)
for y in range(len(rows)):
    for x in range(len(rows[y])):
        for i in range(c.getNumberOfCities()):
            if c.getCityCoord(i) == (x,y) and rows[y][x] != " " and rows[y][x] != "-" and rows[y][x] != ".":
                print(c.getCityName(i) + " is located at x = " + str(x) + " and y = " + str(y))
