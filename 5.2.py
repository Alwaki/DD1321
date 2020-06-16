# Course: DD1321 2019
# Student: Alexander Wallén Kiessling
# Project: Lab A
# Date: 9 June 2020
# Description: A program which defines a greedy best first algorothm, and uses it
# to find the best route between cities on an imported map file. Reworked version.

# SETUP
# ---------------------

# Import packages
from Alexander import *
from classes import *

# Create instances
c = MapEdges()

# Cities to be inspected
cities = ["Haran","Fangorn","Ashdrift","Brilthor","Ruhr","Mount Nevermind","Zhaman","Ship's Haven","Hillfar","Legolin","Oakheart","Doonatel"]

# Create variables
visited = []
startCity = Node(c.getCityIndex(cities[2]), 0)
endCity = Node(c.getCityIndex(cities[3]), 0)

# Create priority queue with huge cost for all nodes
m = minHeap()
for city in c.cities:
    node = Node(c.getCityIndex(city), 10000)
    m.insert(node)

# Remove and reinsert starting node with 0 cost
m.remove(startCity.data)
m.insert(startCity)

# FUNCTION DEFINITIONS
# ---------------------

# Description: A function to investigate the locally cheapest path alternatives from point A to B.
# In: The the ending city (in node form)
# Out: Either a None (result of no path) or the end city in Node form, with attached parents
def pathFindCheap(goal):
    while not m.isEmpty():
        current = m.delMin()
        if current.data != goal.data:
            visited.append(current.data)
            neighbors = c.getNeighborsTo(current.data)
            for i in neighbors:
                if i not in visited:
                    cost = c.getCostBetween(current.data, i)
                    m.remove(i)
                    m.insert(Node(i, cost, current))
        if current.data == goal.data:
            return current
    return None

# Description: A function which develops a node's parents into list form, revealing a path
# In: A node of the last city in the parent chain (given from pathFindBest()), as well as an empty list
# Out: A list with the travel path of cities in inverse order
def pathWriteCheap(city, path):
    if city != None:
        path.append(city.data)
        pathWriteCheap(city.parent, path)
    return path

# Description: A function which calculates the total travel cost of a path.
# In: The last city in the travel path (in Node form), as well as the initial start point
# Out: The total cost of travel (string), or if no path availible, string "infinite"
def totalCost(city, start):
    try:
        totalcost = 0
        while city.data != start.data:
            cost = c.getCostBetween(city.data, city.parent.data)
            city = city.parent
            totalcost += cost
        return str(totalcost)
    except:
        return "infinite"

# DRIVER CODE
# ---------------------
city = pathFindCheap(endCity)
path = pathWriteCheap(city,[])
path.reverse()
if path == []:
    path = "unavailible"
print("The path between the two cities is " + str(path) + ". This totals " + str(len(path)) + " cities.")
print("The cost of travelling the path is " + totalCost(city, startCity) + " sesterces.")
print("Total nodes treated was " + str(len(visited)) + " nodes.")
