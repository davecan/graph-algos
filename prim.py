# Prim's algorithm for minimum spanning tree

from queue import PriorityQueue
import graph2


# Given adjacency list and starting node, 
# returns list of tree edge tuples: (u, v, weight).
def prim(Adj, S):
    visited = [S]
    tree = []
    fringe = PriorityQueue()
    # weight is put first in this tuple so the priority queue can keep track of it
    for v,w in Adj[S].items():
        fringe.put( (w,S,v) )   # (weight, u, v)

    while not fringe.empty():
        weight,u,v = fringe.get()
        if (u,v) not in tree and v not in visited:
            tree.append((u,v,weight))
            visited.append(v)
            for t,w in Adj[v].items():
                fringe.put( (w,v,t) )

    return tree


MST = prim(graph2.Adj, "A")
print("MST:", MST)
print("MST weight:", sum([edge[2] for edge in MST]))