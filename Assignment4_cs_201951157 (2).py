
# Add a vertex to the set of vertices and the graph
def add_vertex(v):
    global graph
    global vertices_no
    global vertices
    if v in vertices:
        print("Vertex ", v, " already exists")
    else:
        vertices_no = vertices_no + 1
        vertices.append(v)
        if vertices_no > 1:
            for vertex in graph:
                vertex.append(0)
        temp = []
        for i in range(vertices_no):
            temp.append(0)
    graph.append(temp)

# Add an edge between vertex v1 and v2 with edge weight e
def add_edge(v1, v2, e):
    global graph
    global vertices_no
    global vertices
    # Check if vertex v1 is a valid vertex
    if v1 not in vertices:
        print("Vertex ", v1, " does not exist.")
    # Check if vertex v1 is a valid vertex
    elif v2 not in vertices:
        print("Vertex ", v2, " does not exist.")
    # Since this code is not restricted to a directed or 
    # an undirected graph, an edge between v1 v2 does not
    # imply that an edge exists between v2 and v1
    else:
        index1 = vertices.index(v1)
        index2 = vertices.index(v2)
        graph[index1][index2] = e

# Print the graph
def print_graph():
    global graph
    global vertices_no
    for i in range(vertices_no):
        for j in range(vertices_no):
            if graph[i][j] != 0:
                   print(vertices[i], " - ", vertices[j], "edge weight: ", graph[i][j])

# Driver code        
# stores the vertices in the graph
vertices = []
# stores the number of vertices in the graph
vertices_no = 0
graph = []
# Add vertices to the graph
add_vertex(1)
add_vertex(2)
add_vertex(3)
add_vertex(4)
add_vertex(5)
# Add the edges between the vertices by specifying
# the from and to vertex along with the edge weights.
add_edge(1, 2, 5)
add_edge(1, 4, 6)
add_edge(2, 1, 5)
add_edge(2, 4, 8)
add_edge(4, 1, 6)
add_edge(4, 2, 8)
add_edge(4, 3, 2)
add_edge(4, 5, 9)
add_edge(3, 4, 2)
add_edge(3, 5, 4)
add_edge(5, 4, 9)
add_edge(5, 3, 4)
print_graph()
print("Internal representation: ", graph)

















from collections import defaultdict
from collections import deque
import math
#global x[[]];

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
    def add_edge(self, u, v):
        self.graph[u].append(v)
    def printAllPathsUtil(self, u, d, visited, path):
        visited[u]= True
        path.append(u)
        if u == d: 
            l = len(path)-1
            str1 = "" 
            for ele in path: 
                str1 += str(ele) + "-"
            parent[l] = str1 
            # m = min(m,l)
            print (path,"  ",(l))
        else:
            for i in self.graph[u]:
                if visited[i]== False:
                    #c= c+1;
                    self.printAllPathsUtil(i, d, visited, path)      
        path.pop()
        visited[u]= False

  
    def printAllPaths(self, s, d):
        visited =[False]*(self.V)
        path = []
        c=0;
        self.printAllPathsUtil(s, d, visited, path)
g = Graph(6)
g.add_edge(1, 2)
g.add_edge(1, 4)
g.add_edge(2, 1)
g.add_edge(2, 4)
g.add_edge(3, 4)
g.add_edge(3, 5)
g.add_edge(4, 1)
g.add_edge(4, 2)
g.add_edge(4, 3)
g.add_edge(4, 5)
g.add_edge(5, 4)
g.add_edge(5, 3)
m=math.inf
s = 1 ; d = 5
frontier = deque()
parent = {}
costdict = {}
print ("Following are all different paths from % d to % d, with Number of Hopes between them :" %(s, d))
g.printAllPaths(s, d)

# now finding the shortest path in the dectionary
for hop,path in parent.items():
   m = min(m,hop)

# for path,hop in parent.items():
# print(parent)
# print(graph)
cost = [[0,5,0,6,0],
     [5,0,0,8,0],
     [0,0,0,2,4],
     [6,8,2,0,9],
     [0,0,4,9,0]]
print("The minimum Numbers of Hop:" ,m)
# print(m)
for hop,path in parent.items():
  if(m==hop):
    pathlist = list(path.split("-"))
    pathlist.pop()
    for i in range(0,len(pathlist)):
      pathlist[i] = (int)(pathlist[i])
    print("The Path containing Minimum hops ",pathlist)
    cost1 = 0
    print(len(pathlist))
    for i in range(len(pathlist)-1):
      cost1 = cost1 + cost[pathlist[i]-1][pathlist[i+1]-1]

    costdict[cost1] = str(pathlist)
    # print(cost1)




mini = math.inf
for cost,path in costdict.items():
  #  print(cost)
  mini = min(mini,cost)

print(mini)
for cost,path in costdict.items():
   if(cost==mini):
     print(path, " cost is ", cost)

print(x)

graph

def add_vertex(v):
    global graph
    global vertices_no
    global vertices
    if v in vertices:
        print("Vertex ", v, " already exists")
    else:
        vertices_no = vertices_no + 1
        vertices.append(v)
        if vertices_no > 1:
            for vertex in graph:
                vertex.append(0)
        temp = []
        for i in range(vertices_no):
            temp.append(0)
    graph.append(temp)