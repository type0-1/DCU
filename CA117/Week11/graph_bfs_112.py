class Graph(object):

    def __init__(self, V):
        self.V = V
        self.adj = {}

        for i in range(V):
            self.adj[i] = []
        
    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)
    
    def degree(self, v):
        return len(self.adj[v])
    
    def maxDegree(self):
        return max([len(self.adj[i]) for i in self.adj])
    
    def avgDegree(self):
        degrees = [len(self.adj[i]) for i in self.adj]
        return sum(degrees) / len(degrees)

class BFSPaths(object):

    def __init__(self, g, s):
        self.g = g
        self.s = s

        self.visited = [False] * g.V 
        self.marked = [-1] * g.V 
        self.bfs(s)

    def bfs(self, s):

        queue = [s]
        self.visited[s] = True

        while queue != []:
            vertex = queue.pop(0)
            for node in self.g.adj[vertex]:
                if self.visited[node] == False:
                    self.marked[node] = vertex
                    queue.append(node)
                    self.visited[node] = True
                

        
    def hasPathTo(self, v):
        return self.visited[v]
    
    def pathTo(self, v):

        if not self.hasPathTo(v):
            return []
        
        path = [v]

        while v != self.s:
            v = self.marked[v]
            path.append(v)
        
        return path[::-1]
