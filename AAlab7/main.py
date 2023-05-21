import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from timeit import default_timer as timer
from graph import Graph
import random

# Initialize a simple graph with only 2 nodes connected between them
new_graph = Graph()
new_graph.add_vertex(1)
new_graph.add_vertex(2)
new_graph.add_edge(1, 2, weight=random.randint(1, 50))
vertex_index = 3

prim_times = []
kruskal_times = []

for i in range(100):
    new_graph.add_vertex(vertex_index)
    new_graph.add_edge(vertex_index, random.randint(1,vertex_index - 1), weight=random.randint(1, 50))

    for i in range(40):
        rnd1 = random.randint(1, vertex_index)
        while vertex_index == rnd1:
            rnd1 = random.randint(1, vertex_index)

        new_graph.add_edge(vertex_index, rnd1, weight=random.randint(1, 50))

    start_time1 = timer()
    new_graph.prim_mst()
    prim_times.append(timer() - start_time1)

    start_time2 = timer()
    new_graph.kruskal_mst()
    kruskal_times.append(timer() - start_time2)

    vertex_index += 1


vertex_list = [x for x in range(2,vertex_index - 1)]

plt.plot(vertex_list, prim_times)
plt.plot(vertex_list, kruskal_times)
plt.xlabel('Number of vertices')
plt.ylabel('Seconds elapsed')
plt.legend(['prim times', 'kruskal times'])
plt.show()