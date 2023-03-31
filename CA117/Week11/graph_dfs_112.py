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

class DFSPaths(object):

    def __init__(self, g, s):
        self.g = g
        self.s = s

        self.visited = [False] * g.V
        self.parent = [-1] * g.V 
        self.dfs(s)
    
    def dfs(self, v):

        self.visited[v] = True
        
        for node in self.g.adj[v]:
            if not self.visited[node]:
                self.parent[node] = v
                self.dfs(node)
    
    def hasPathTo(self, v):
        return self.visited[v]
    
    def pathTo(self, v):

        if not self.hasPathTo(v):
            return []
        
        path = [v]

        while v != self.s:
            v = self.parent[v]
            path.append(v)
        
        return path[::-1]
