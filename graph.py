#Author: Jasmeen Kaur
#Date: March 15, 2023
#Title : graph.py

class Vertex:
    def __init__(self,key,value=''):
        self.id = key
        self.connectedTo = {}
        self.color = 'white'


    def add_neighbor(self, neighbor, w = 0):
        self.connectedTo[neighbor] = w

    def __str__(self):
        return f'{self.id} connected to: {[v.id for v in self.connectedTo]}'

    def get_connections(self):
        return self.connectedTo.keys()

    def get_id(self):
        return self.id

    def get_value(self,neighbor):
        return self.connectedTo[neighbor]

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def add_vertex(self, key,):
        self.numVertices += 1
        vertex = Vertex(key)
        self.vertList[key] = vertex
        return vertex

    def get_vertex(self, hello):
        if hello in self.vertList:
            return self.vertList[hello]
        else:
            return None
        
    def __contains__(self, hello):
        return hello in self.vertList

    def add_edge(self, f, t):
        if f not in self.vertList:
            self.add_vertex(f)
        if t not in self.vertList:
            self.add_vertex(t)
        self.vertList[f].add_neighbor(self.vertList[t])
        self.vertList[t].add_neighbor(self.vertList[f])

    def get_vertices(self):
        return (self.vertList.keys())

   
    def __iter__(self):
        return iter(self.vertList.values())
    
def breadth_first_search(self, s):
    # vertices = white
    for v in self.vertList.values():
        v.color = 'white'
    
    queue = []
    path = []
    start = self.vertList[s]

    start.color = 'gray'
    queue.append(start)
    path.append(start.id)
    
    while len(queue) != 0:
        # dequeue
        v = queue.pop(0)
        for u in v.connectedTo.keys():
            if u.color == 'white':
                u.color = 'gray'
                queue.append(u)
                path.append(u.id)
        
        # mark dequeued vertex as black
        v.color = 'black'
    
    #return path
    return path

def depth_first_search(self):
    #vertices = white
    for v in self.vertList.values():
        v.color = 'white'
    
    path = []
    for v in self.vertList.values():
        if v.color == 'white':
            # dfs
            self.DFS(v.id, path)
    
    #path
    return path

def DFS(self, vid, path):

    v = self.vertList[vid]
    v.color = 'gray'
    
    #vertex + path
    path.append(v.id)
    
    for u in v.connectedTo.keys():
        if u.color == 'white':
            self.DFS(u.id, path)
    
    v.color = 'black'
    
    return path





