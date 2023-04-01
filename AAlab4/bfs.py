import getGraphs as GG
import networkx as nx

def bfs(graph, start):
    visited = set()
    queue = [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            neighbors = list(graph.neighbors(vertex))
            queue.extend([node for node in neighbors if node not in visited])
    return visited

