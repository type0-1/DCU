import sys

lines = sys.stdin.readlines()
v, edges = int(lines[0].strip()), lines[1:]
graph = {i : [] for i in range(v)}
visited = [False] * v
islands = 0

def depth_first_search(vertex):
    visited[vertex] = True
    for node in graph[vertex]:
        if not visited[node]:
            depth_first_search(node)
            
for edge in edges:
    vertex, node = [int(n) for n in edge.strip().split()]
    graph[vertex].append(node)
    graph[node].append(vertex)

for i in range(v):
    if not visited[i]:
        islands += 1
        depth_first_search(i)
        
print(islands)
