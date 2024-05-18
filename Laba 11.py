# Задание 1

def dijkstra(G, n0, n_end = None):
    dist = {v: float('infinity') for v in G}
    dist[n0] = 0
    queue = [(n0, 0)]
    visited = set()
    parents = {v: None for v in G}

    while queue:
        v0, d0 = min(queue, key=lambda x: x[1])
        visited.add(v0)
        queue.remove((v0, d0))
        if d0 > dist[v0]:
            continue
        for v1, w1 in G[v0].items():
            d01 = d0 + w1['weight']
            if d01 < dist[v1]:
                dist[v1] = d01
                queue.append((v1, d01))
                parents[v1] = v0
        if n_end and all(n in visited for n in G[n_end].keys()):
            res = []
            v = n_end
            while v != None:
                res.append(v)
                v = parents[v]
            return dist[n_end], res[::-1]

    return dist, parents

# Задание 2

import networkx as nx

G = nx.fast_gnp_random_graph(6, 0.5, seed=1237)
weights = [1,3,2,3,1,1,6,1]
w_dict = {}
for i,e in enumerate(G.edges):
    w_dict[e] = weights[i]
nx.set_edge_attributes(G, w_dict, 'weight')

def draw(G):
    layout = nx.kamada_kawai_layout(G);
    nx.draw_networkx_nodes(G, pos=layout);
    nx.draw_networkx_edges(G, pos=layout, alpha=0.2);
    nx.draw_networkx_labels(G, pos=layout, labels={i: str(i) for i in G.nodes})
    nx.draw_networkx_edge_labels(G, pos=layout, edge_labels={i: G.edges[i]['weight'] for i in G.edges});

draw(G)

d, p_list = dijkstra(G, 3, 5)
print(p_list, d)
	
# Задание 3

import matplotlib.pyplot as plt

def graphical_dijkstra(G, n0, n_end = None):
    dist = {v: float('infinity') for v in G}
    dist[n0] = 0
    queue = [(n0, 0)]
    visited = set()
    parents = {v: None for v in G}

    layout = nx.kamada_kawai_layout(G);
    plt.figure(figsize=(10,7))
    nx.draw_networkx_nodes(G, pos=layout, node_color = [(0,0,1)]);
    nx.draw_networkx_edges(G, pos=layout, alpha=0.2);
    nx.draw_networkx_labels(G, pos=layout, labels={i: str(i) + ': ' + str(dist[i]) for i in G.nodes})
    nx.draw_networkx_edge_labels(G, pos=layout, edge_labels={i: G.edges[i]['weight'] for i in G.edges});
    plt.show()
    input()

    while queue:
        v0, d0 = min(queue, key=lambda x: x[1])
        visited.add(v0)
        queue.remove((v0, d0))
        if d0 > dist[v0]:
            continue
        for v1, w1 in G[v0].items():
            d01 = d0 + w1['weight']
            if d01 < dist[v1]:
                dist[v1] = d01
                queue.append((v1, d01))
                parents[v1] = v0
        plt.figure(figsize=(10,7))
        nx.draw_networkx_nodes(G, pos=layout, node_color = [(1,0,0) if v0 == i else (0,1,0) if i not in visited else (0,0,1) for i in G.nodes]);
        nx.draw_networkx_edges(G, pos=layout, alpha=0.2);
        nx.draw_networkx_edges(G, pos=layout, edgelist =[(v0, v1) for v0,v1 in parents.items() if v1 is not None], arrows = True, arrowstyle = '<|-', alpha=0.5);
        nx.draw_networkx_labels(G, pos=layout, labels={i: str(i) + ': ' + str(dist[i]) for i in G.nodes})
        nx.draw_networkx_edge_labels(G, pos=layout, edge_labels={i: G.edges[i]['weight'] for i in G.edges});
        plt.show()
        input()
        if n_end and all(n in visited for n in G[n_end].keys()):
            res = []
            v = n_end
            while v != None:
                res.append(v)
                v = parents[v]
            return dist[n_end], res[::-1]
    return dist, parents

d, p_list = graphical_dijkstra(G, 3, 5)
p_list, d

# Задание 4


import networkx as nx
from random import random, seed
seed(1234)

G = nx.barbell_graph(5, 1)
communities_generator = nx.community.girvan_newman(G)
top_level_communities = next(communities_generator)
next_level_communities = next(communities_generator)
layout = nx.kamada_kawai_layout(G);

for comm in sorted(map(sorted, next_level_communities)):
    color = (random(), random(), random())
    nx.draw_networkx_nodes(G, pos=layout, nodelist = comm, node_color = color);
nx.draw_networkx_edges(G, pos=layout, alpha=0.2);