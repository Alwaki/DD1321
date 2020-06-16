#Course: DD1321 2019
#Student: Alexander Wallén Kiessling
#Project: Lab A

#Import packages
from Alexander import *
from classes import *

#create instances
c = MapEdges()
m = minHeap()

#cities to be inspected
cities = ["Haran","Fangorn","Ashdrift","Brilthor","Ruhr","Mount Nevermind","Zhaman","Ship's Haven","Hillfar","Legolin","Oakheart","Doonatel"]

#define variables
startCity = c.getCityIndex(cities[2])
endCity = c.getCityIndex(cities[3])
visited = []
complexCounter = 0

#DESC: A function to investigate the cheapest path alternatives from point A to B
#IN: The starting city as well as the ending city (integers)
#OUT: Either a None (result of no path) or the end city in Node form, with attached parents
def pathFindBest(startCity, endCity):
    city = Node(startCity, 0)
    m.insert(city)
    while city.data != endCity and not m.isEmpty():
        city = m.delMin()
        visited.append(city.data)
        neighbors = c.getNeighborsTo(city.data)
        for i in neighbors:
            if i not in visited:
                global complexCounter
                complexCounter += 1
                cost = c.getCostBetween(city.data, i)
                m.insert(Node(i, cost, city))
                visited.append(i)
    if m.isEmpty():
        return None
    else:
        return city

#DESC: A function which develops a node's parents into list form, revealing a path
#IN: A node of the last city in the parent chain (given from pathFindBest()), as well as an empty list
#OUT: A list with the travel path of cities in inverse order
def pathWriteBest(city, path):
    if city != None:
        path.append(city.data)
        pathWriteBest(city.parent, path)
    return path

#DESC: A function which calculates the total travel cost of a path.
#IN: The last city in the travel path (in Node form), as well as the initial start point
#OUT: The total cost of travel (string), or if no path availible, string "infinite"
def totalCost(city, start):
    try:
        totalcost = 0
        while city.data != start:
            cost = c.getCostBetween(city.data, city.parent.data)
            city = city.parent
            totalcost += cost
        return str(totalcost)
    except:
        return "infinite"

#driver code
city = pathFindBest(startCity, endCity)
path = pathWriteBest(city,[])
path.reverse()
if path == []:
    path = "unavailible"
print("The path between the two cities is " + str(path) + ". This totals " + str(len(path)) + " cities.")
print("The cost of travelling the path is " + totalCost(city,startCity) + " sesterces.")

#Check how many nodes left in queue
counter = 0
while not m.isEmpty():
    m.delMin()
    counter += 1

print("The amount of nodes left in the queue was " + str(counter) + ".")
print("Total nodes treated was " + str(len(visited)) + " nodes.")
print("Complexity result: " + str(complexCounter))
