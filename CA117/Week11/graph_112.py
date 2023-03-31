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