# Course: DD1321 2019
# Student: Alexander Wallén Kiessling
# Project: Lab A
# Date: 1 July 2020
# Description: A program which defines a greedy best first algorothm, and uses it
# to find the best route between cities on an imported map file. Reworked version.
# Includes a debugging setting for further information.

# SETUP
# ---------------------

# Import packages
from Alexander import *
from classes import *

# Create instances
c = MapEdges()

# Set debugging mode on or off, which releases prints regarding status of algorithm
Debugging = False

# Testing prints
if Debugging:
    print("--------------------------------------------")
    print("The correct path is (for Haran to Fangorn): ")
    print("Haran: 80, Goldenleaf: 20, Lochley: 34, Merriwich: 74, Shiny Ship: 40,",
        "Northtown: 61, Death's Door: 11, Doveseal: 37, The Last Battle: 50, Ergoth: 23,",
        "Trudid: 41, Fangorn: 63", sep = "\n")
    truecost = c.getCostBetween(80, 20) + c.getCostBetween(20, 34) + c.getCostBetween(34, 74) + c.getCostBetween(74, 40) + c.getCostBetween(40, 61) + c.getCostBetween(61, 11) + c.getCostBetween(11, 37) + c.getCostBetween(37, 50) + c.getCostBetween(50, 23) + c.getCostBetween(23, 41) + c.getCostBetween(41, 63)
    print("The true cost of travelling should be: " + str(truecost))
    print("--------------------------------------------")
    print("Current information is: ")
    # Check
    investigating = 40
    print(c.getNeighborsTo(investigating))
    x = c.getNeighborsTo(investigating)
    for i in x:
        print("The cost between city: " + str(investigating) + " and " + "city " + str(i) + " is: " + str(c.getCostBetween(i,investigating)))
    print("--------------------------------------------")
# End of testing prints

# Cities to be inspected
cities = ["Haran","Fangorn","Ashdrift","Brilthor","Ruhr","Mount Nevermind","Zhaman","Ship's Haven","Hillfar","Legolin","Oakheart","Doonatel"]

# Create variables, change cities index depending on start and destination
visited = {} #initialize hashtable
startCity = Node(c.getCityIndex(cities[0]), 0)
endCity = Node(c.getCityIndex(cities[1]), 0)
#endCity = Node(61, 0)

# Create priority queue with huge cost for all nodes
m = minHeap()
for city in c.cities:
    name = city[0]
    node = Node(c.getCityIndex(name), 10000)
    m.insert(node)

# Remove and reinsert starting node with 0 cost
m.remove(startCity.data)
m.insert(startCity)

# FUNCTION DEFINITIONS
# ---------------------

# Description: A function to investigate the cheapest path alternatives from point A to B.
# In: The goal city (in node form)
# Out: Either a None (result of no path) or the end city in Node form, with attached parents
def pathFindCheap(goal):
    while not m.isEmpty():
        current = m.delMin()

        if Debugging:
            print("The current city is: " + str(current.data))
            print("The cost of this current path is: " + str(current.priority))

        visited[current.data] = current.priority
        neighbors = c.getNeighborsTo(current.data)
        for i in neighbors:
            cost = c.getCostBetween(current.data, i) + current.priority
            if i not in visited:
                m.remove(i)
                node = Node(i, cost, current)

                if Debugging:
                    print("Adding city " + str(i) + " with cost " + str(cost))

                visited[node.data] = node.priority
                m.insert(node)
            elif i in visited and cost < visited[i]:
                m.remove(i)
                node = Node(i, cost, current)

                if Debugging:
                    print("Replacing city " + str(i) + " with cost " + str(cost))

                visited[node.data] = node.priority
                m.insert(node)
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
# In: The last city in the travel path (in Node form)
# Out: The total cost of travel (string), or if no path availible, string "infinite"
def totalCost(city):
    try:
        return str(city.priority)
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
print("The cost of travelling the path is " + totalCost(city) + " sesterces.")
print("Total nodes treated was " + str(len(visited)) + " nodes.")
