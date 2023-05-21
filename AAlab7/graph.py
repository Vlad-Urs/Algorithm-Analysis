import networkx as nx
import matplotlib.pyplot as plt
import sys

class Graph:
    def __init__(self):
        self.G = nx.Graph()
        self.V = len(self.G.nodes)

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


    def minKey(self, key, mstSet):
        # Initialize min value
        min_index = 0
        min = sys.maxsize
        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v
        return min_index

    # Function to construct and print MST for a graph
    # represented using adjacency matrix representation
    def prim_mst(self):
        # Key values used to pick minimum weight edge in cut
        key = [sys.maxsize] * self.G.number_of_nodes()
        parent = [None] * self.G.number_of_nodes()  # Array to store constructed MST
        # Make key 0 so that this vertex is picked as first vertex
        key[0] = 0
        mstSet = [False] * self.G.number_of_nodes()
        parent[0] = -1  # First node is always the root of
        for cout in range(self.G.number_of_nodes()):
            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # u is always equal to src in first iteration
            u = self.minKey(key, mstSet)
            # Put the minimum distance vertex in
            # the shortest path tree
            mstSet[u] = True
            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shortest path tree
            for v in range(self.G.number_of_nodes()):
                # graph[u][v] is non zero only for adjacent vertices of m
                # mstSet[v] is false for vertices not yet included in MST
                # Update the key only if graph[u][v] is smaller than key[v]
                if self.G.has_edge(u, v) and mstSet[v] == False \
                and key[v] > self.G[u][v]['weight']:
                    key[v] = self.G[u][v]['weight']
                    parent[v] = u
        result = []
        for i in range(1, self.G.number_of_nodes()):
            result.append([parent[i], i, key[i]])
        return result

    def kruskal_mst(self):
        edges = sorted(self.G.edges(data=True), key=lambda x: x[2]['weight'])
        parents = {v: v for v in self.G.nodes()}
        ranks = {v: 0 for v in self.G.nodes()}
        mst = []

        def find(v):
            if parents[v] != v:
                parents[v] = find(parents[v])
            return parents[v]

        def union(u, v):
            u_root, v_root = find(u), find(v)
            if u_root == v_root:
                return False
            if ranks[u_root] < ranks[v_root]:
                parents[u_root] = v_root
            elif ranks[u_root] > ranks[v_root]:
                parents[v_root] = u_root
            else:
                parents[v_root] = u_root
                ranks[u_root] += 1
            return True

        for edge in edges:
            u, v, data = edge
            if union(u, v):
                mst.append(edge)

        return mst