# Converts graph to DAG by removing all back edges.
# Topologically orders the DAG two ways:
#    DFS using start/finish times
#    BFS

from DFS import DFS
from BFS import BFS
import graph1


def remove_backedges(G):
    dfs = DFS(G)
    dfs.search()
    dfs.classify_edges()
    print("Back Edges: " + str(dfs.back_edges))

    dag = G
    for u in dag:
        for v in dag[u]:
            if (u,v) in dfs.back_edges:
                dag[u].remove(v)
    print("DAG: " + str(dag))
    return dag


def dfs_topo(dag):
    dfs = DFS(dag)
    dfs.search()
    print("DFS Tree: " + str(dfs.tree_edges))
    print("Times: " + str(dfs.times()))

    # topological order
    # it doesn't need a separate stack thanks to set comprehensions
    fin = {e[1]:n for n,e in dfs.times().items()}  # dictionary of key = finish time, val = node name
    topo = []
    for k in reversed(sorted(fin.keys())):   # reverse order by finish time
        topo.append(fin[k])
    print("DFS Topo: " + ' '.join(topo))
    return topo


# adapted from https://www.quora.com/Can-topological-sorting-be-done-using-BFS
def bfs_topo(dag):
    # find all nodes with in-degree of 0  (only A in graph1)
    in_deg = {x:0 for x in dag}
    for u in dag:
        for v in dag[u]:
            in_deg[v] += 1
    zeros = [k for k,v in in_deg.items() if v == 0]
    topo = []

    # visit each zero-degree node
    # remove it from the graph, prune its edges, reduce in-degree of touched nodes,
    # and visit a zero-degree child and continue
    while zeros:
        u = zeros.pop(0)
        topo.append(u)
        for v in dag[u]:
            in_deg[v] -= 1
            if in_deg[v] == 0:
                zeros.append(v)
    return topo



dag = remove_backedges(graph1.Adj)
print('dag',dag)
topo = dfs_topo(dag)
print("BFS Topo: " + ' '.join(bfs_topo(dag)))