# Dijkstra's shortest path algorithm

from queue import PriorityQueue
import sys

# graph adjacency list
A='A';B='B';C='C';D='D';E='E';F='F'

Adj = { A: { B:5, C:3, D:1 }, 
        B: { C:1, D:3 },
        C: { B:3, D:7, E:1 }, 
        D: { A:6, C:3 },
        E: { F:5 },
        F: { D:3, A:4 } }

def dijkstra(Adj, S):
    dist = {}
    visited = []
    queue = PriorityQueue()
    for v in Adj:
        dist[v] = sys.maxsize
        queue.put((dist[v],v))
        print("queued (%s,%s)" % (dist[v],v))
    dist[S] = 0
    print("initial distance:", dist)
    
    while not queue.empty():
        print('='*10)
        cur_dist,u = queue.get()
        print("u =", u)
        for v in Adj[u]:
            weight = Adj[u][v]
            print('-'*10)
            print("v =", v)
            print("dist[%s] = %s" % (v, dist[v]))
            print("dist[%s] = %s, weight = %s" % (u, dist[u], weight))
            if dist[v] > dist[u] + weight:   # process the triple
                dist[v] = dist[u] + weight   # relaxation
                print("relaxed %s to %s" % (v, dist[v]))
            print("dist:", dist)
    return dist


paths = dijkstra(Adj,"A")
print(paths)