from bfs import bfs
from dfs import dfs
import getGraphs as GG
from timeit import default_timer as timer
import matplotlib.pyplot as plt

balanced_graphs = [GG.b1, GG.b2, GG.b3]
unbalanced_graphs = [GG.u1, GG.b2, GG.u3]

balanced_times_dfs = []
unbalanced_times_dfs = []
balanced_times_bfs = []
unbalanced_times_bfs = []

vertices_numbers = [5,10,20]


for graph in balanced_graphs:
    start_time = timer()
    dfs(graph,0)
    balanced_times_dfs.append(timer()-start_time)

    start_time = timer()
    bfs(graph, 0)
    balanced_times_bfs.append(timer() - start_time)


for graph in unbalanced_graphs:
    start_time = timer()
    dfs(graph,0)
    unbalanced_times_dfs.append(timer()-start_time)

    start_time = timer()
    bfs(graph, 0)
    unbalanced_times_bfs.append(timer() - start_time)

print(balanced_times_dfs)
print(balanced_times_bfs)
plt.plot(vertices_numbers,balanced_times_dfs)
plt.plot(vertices_numbers,balanced_times_bfs)
plt.xlabel('Number of vertices')
plt.ylabel('Seconds elapsed')

print(unbalanced_times_dfs)
print(unbalanced_times_bfs)
plt.plot(vertices_numbers,unbalanced_times_dfs)
plt.plot(vertices_numbers,unbalanced_times_bfs)
plt.legend(['balanced dfs','balanced bfs'])
plt.legend(['balanced dfs','balanced bfs','unbalanced dfs','unbalanced bfs'])
plt.show()






