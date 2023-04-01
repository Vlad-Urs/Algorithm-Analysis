import networkx as nx
import matplotlib.pyplot as plt


# balanced 1
b1 = nx.Graph()
with open('graphs/balanced1.txt', 'r') as f:
    for line in f:
        u, v = map(int, line.strip().split())
        b1.add_edge(u, v)

# plot the graph
nx.draw(b1, with_labels=True)
plt.show()


# unbalanced 1
u1 = nx.Graph()
with open('graphs/unbalanced1.txt', 'r') as f:
    for line in f:
        u, v = map(int, line.strip().split())
        u1.add_edge(u, v)

# plot the graph
nx.draw(u1, with_labels=True)
plt.show()


# balanced 2
b2 = nx.Graph()
with open('graphs/balanced2.txt', 'r') as f:
    for line in f:
        u, v = map(int, line.strip().split())
        b2.add_edge(u, v)

# plot the graph
nx.draw(b2, with_labels=True)
plt.show()


# unbalanced 2
u2 = nx.Graph()
with open('graphs/unbalanced2.txt', 'r') as f:
    for line in f:
        u, v = map(int, line.strip().split())
        u2.add_edge(u, v)

# plot the graph
nx.draw(u2, with_labels=True)
plt.show()


# balanced 3
b3 = nx.Graph()
with open('graphs/balanced3.txt', 'r') as f:
    for line in f:
        u, v = map(int, line.strip().split())
        b3.add_edge(u, v)

# plot the graph
nx.draw(b3, with_labels=True)
plt.show()


# unbalanced 3
u3 = nx.Graph()
with open('graphs/unbalanced3.txt', 'r') as f:
    for line in f:
        u, v = map(int, line.strip().split())
        u3.add_edge(u, v)

# plot the graph
nx.draw(u3, with_labels=True)
plt.show()