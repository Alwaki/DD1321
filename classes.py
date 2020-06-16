#Course: DD1321 2019
#Student: Alexander Wallén Kiessling
#Project: Lab A

#Create node class with comparison methods
class Node:
    def __init__(self, data, priority, parent = None):
        self.data = data
        self.priority = priority
        self.parent = parent #added parent to keep track of path

    def __eq__(self,other):
        try:
            return self.priority == other.priority
        except:
            return None

    def __lt__(self, other):
        try:
            return self.priority < other.priority
        except:
            return None

    def __gt__(self, other):
        try:
            return self.priority > other.priority
        except:
            return None

#Create priority queue class, structured as min heap
class minHeap:
    def __init__(self):
        self.veksize = 1024  #declare appropriate size of heap vector
        self.vek = [None] * (self.veksize)   #declare vector for heap
        self.pos = 0   #define current pos, with starting index 0

    def isEmpty(self):
        return self.pos  == 0

    def insert(self, node):
            self.pos += 1
            self.vek[self.pos] = node
            i = self.pos
            while i > 1 and self.vek[i//2] > self.vek[i]: #if parent greater, switch place
                temp = self.vek[i] #temporary storage of node
                self.vek[i] = self.vek[i//2]
                self.vek[i//2] = temp
                i = i//2 #iterate to parent

    #fixed sorting error for reworked version
    def sortHeap(self, i):
        if not self.isEmpty():
            if self.vek[i] < self.vek[i//2]:
                temp = self.vek[i] #temporary storage of node                    self.vek[i] = self.vek[i//2]
                self.vek[i] = self.vek[i//2]
                self.vek[i//2] = temp
            if i > 1:
                self.sortHeap(i - 1) #recursively sort rest of heap by calling function again

    #fixed removal error for reworked version
    def delMin(self):
        if not self.isEmpty(): #pop smallest, then resort heap
            minNode = self.vek[1]
            self.vek[1] = self.vek[self.pos]
            self.vek[self.pos] = None
            self.pos -= 1
            self.sortHeap(self.pos)
            return minNode
        else:
            return None

    #added "remove" functionality for 5.2 greedy best first reworked version
    def remove(self, key):
        for i in range(self.veksize):
            try:
                if self.vek[i].data == key:
                    temp = self.vek[self.pos]
                    self.vek[self.pos] = self.vek[i]
                    self.vek[i] = temp
                    self.vek[self.pos] = None
                    self.pos -= 1
                    self.sortHeap(self.pos)
                    break
            except:
                pass
