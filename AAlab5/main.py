import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from timeit import default_timer as timer
from graph import Graph
import random


vertices = 100
# Create dense graph
dense_graph = Graph()
for i in range(1,vertices):
    dense_graph.add_vertex(i)
for i in range(1,vertices):
    dense_graph.add_edge(i,i+1, weight = random.randint(1,50))
dense_graph.add_edge(1, 100, weight = random.randint(1,50))
#dense_graph.draw_graph()

for i in range(1,200):
    rnd1 = random.randint(1,101)
    rnd2 = random.randint(1,101)

    if rnd1 != rnd2:
        if (rnd1, rnd2) not in dense_graph.G.edges() or (rnd2, rnd1) not in dense_graph.G.edges():
            dense_graph.add_edge(rnd1, rnd2, weight = random.randint(1, 50))


# Create sparse graph
sparse_graph = Graph()
for i in range(1,vertices):
    sparse_graph.add_vertex(i)
for i in range(1,vertices):
    sparse_graph.add_edge(i,i+1, weight = random.randint(1,50))
sparse_graph.add_edge(1, 100, weight = random.randint(1,50))

for i in range(1,20):
    rnd1 = random.randint(1,101)
    rnd2 = random.randint(1,101)

    if rnd1 != rnd2:
        if (rnd1, rnd2) not in sparse_graph.G.edges() or (rnd2, rnd1) not in sparse_graph.G.edges():
            sparse_graph.add_edge(rnd1, rnd2, weight = random.randint(1, 50))
#sparse_graph.draw_graph()


vertex_list = [100]
FW_times_sparse = []
DK_times_sparse = []
FW_times_dense = []
DK_times_dense = []

for i in range(10):
    vertices += 1
    vertex_list.append(vertices)

    # Starting with the sparse graph
    # start the timer
    start_time1 = timer()
    # call F-W
    #FloydWarshall(sparse_graph.G, vertices)
    sparse_graph.floyd_warshall()
    # record F-W time
    FW_times_sparse.append(timer() - start_time1)

    # start the timer
    start_time2 = timer()
    # call Dijkstra
    sparse_graph.all_shortest_paths()
    # record Dijkstra time
    DK_times_sparse.append(timer() - start_time2)

    # Add a node and connect it to the graph
    sparse_graph.add_vertex(vertices)
    sparse_graph.add_edge(vertices, random.randint(1,vertices - 1), weight = random.randint(1, 50))


    # Moving to the dense graph
    # start the timer
    start_time3 = timer()
    # call F-W
    #FloydWarshall(dense_graph.G, vertices)
    dense_graph.floyd_warshall()
    # record F-W time
    FW_times_dense.append(timer() - start_time3)

    # start the timer
    start_time4 = timer()
    # call Dijkstra
    dense_graph.all_shortest_paths()
    # record Dijkstra time
    DK_times_dense.append(timer() - start_time4)

    # Add a node and connect it to the graph
    dense_graph.add_vertex(vertices)
    dense_graph.add_edge(vertices, random.randint(1, vertices - 1), weight=random.randint(1, 50))


vertex_list.pop(-1)

plt.plot(vertex_list, FW_times_sparse)
plt.plot(vertex_list, FW_times_dense)
plt.plot(vertex_list, DK_times_sparse)
plt.plot(vertex_list, DK_times_dense)
plt.xlabel('Number of vertices')
plt.ylabel('Seconds elapsed')
plt.legend(['sparse F-W', 'dense F-W', 'sparse Dijkstra', 'dense Dijkstra'])
plt.show()



