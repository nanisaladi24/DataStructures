from queue import *

class Node():
    def __init__(self,dataVal=None):
        self.data = dataVal
        self.nextElement = None
class LinkedList:
    def __init__(self):
        self.headval = None
class graph():
    def __init__(self,myvertices):
        self.vertices = myvertices
        self.array = [None]*myvertices

def bfsTraversal(g,source):
 result = ""
 #result = result+str(source)
 num_of_vertices = g.vertices
 # Write - Your - Code
 tempSrc = g.array[source-1]
 myQueue = Queue()
 myQueue.put(source)
 while (not myQueue.empty()):
    temp = myQueue.get()
    result = result+str(temp)
    tempSrc = g.array[temp-1]
    while(tempSrc!=None):
      myQueue.put(tempSrc.data)
      tempSrc=tempSrc.nextElement
      
 return result #For the above graph, it should return "01234" or "02143"

g = graph(5)

myLL = Node(3)
myLL.nextElement = Node(2)

g.array[0]=myLL

myLL = Node(5)
myLL.nextElement = Node(4)

g.array[1]=myLL

g.array[2:5]=[None,None,None]

source = 1

#print (g.array)

print (bfsTraversal(g,source))