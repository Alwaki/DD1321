#Course: DD1321 2019
#Student: Alexander Wallén Kiessling
#Project: Lab A

#Import packages
from Alexander import *

#create instance
c = MapEdges()

#cities to be inspected
cities = ["Haran","Fangorn","Ashdrift","Brilthor","Ruhr","Mount Nevermind","Zhaman","Ship's Haven","Hillfar","Legolin","Oakheart","Doonatel"]

#define variables
startCity = c.getCityIndex(cities[10])
endCity = c.getCityIndex(cities[11])


#DESC: A function intended to find a path between two cities
#IN: starting city and ending city (integers)
#OUT: a dictionary containing successful paths between cities, or none.
def pathFind(startCity, endCity):
    queue = [startCity]
    pathDict = {}
    while queue != None:
        try:
            city = queue.pop(0)
            if city == endCity:
                counter = 0
                while queue != []:
                    counter += 1
                    queue.pop()
                print("Heltal kvar i kön är: " + str(counter) + ".")
                return pathDict
            neighbours = c.getNeighborsTo(city)
            for i in neighbours:
                if i not in pathDict:
                    pathDict[i] = city
                    queue.append(i)
        except:
            break
    return None

#DESC: A function which described a path from A to B as well as resources required to travel.
#IN: A dictionary describing paths taken, the destination (integer) as well as current position (integer)
#OUT: A tuple of the path in list form, and the total cost of travel in integer form
def pathWrite(pathDict, destination, current):
    if pathDict == None:
        return "unavailible","infinite"
    path = [current]
    cost = 0
    while path[-1] != destination:
        last = current
        current = pathDict[current]
        cost = cost + c.getCostBetween(last,current)
        path.append(pathDict[current])
    path.reverse()
    return path,cost

#driver code
results = pathWrite(pathFind(startCity, endCity), startCity, endCity)
print("The path between the two cities is " + str(results[0]) + ". This totals " + str(len(results[0])) + " cities.")
print("The cost of travelling the path is " + str(results[1]) + " sesterces.")
