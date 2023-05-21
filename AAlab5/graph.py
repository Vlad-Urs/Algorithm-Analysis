import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        self.G = nx.Graph()

    def add_vertex(self, v):
        self.G.add_node(v)

    def add_edge(self, u, v, weight = None):
        self.G.add_edge(u, v, weight=weight)

    def draw_graph(self):
        pos = nx.spring_layout(self.G)
        nx.draw(self.G, pos, with_labels=True)
        labels = nx.get_edge_attributes(self.G, 'weight')
        nx.draw_networkx_edge_labels(self.G, pos, edge_labels=labels)
        plt.show()

    def all_shortest_paths(self):
        paths = {}
        nodes = list(self.G.nodes())
        for i in range(len(nodes)):
            for j in range(i + 1, len(nodes)):
                u, v = nodes[i], nodes[j]
                shortest_path = nx.shortest_path(self.G, u, v, weight='weight')
                paths[(u, v)] = shortest_path
                paths[(v, u)] = list(reversed(shortest_path))
        return paths

    def floyd_warshall(self):
        dist = {}
        for u in self.G.nodes():
            dist[u] = {}
            for v in self.G.nodes():
                dist[u][v] = float('inf')
            dist[u][u] = 0
            for v, w in self.G[u].items():
                dist[u][v] = w['weight']

        for k in self.G.nodes():
            for i in self.G.nodes():
                for j in self.G.nodes():
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        return dist