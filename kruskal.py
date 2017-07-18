# Kruskal's algorithm for minimum spanning tree
# adds lowest-weight edges globally from the graph
# like working from a "top-down" view of a video game map w/ every edge visible

from DisjointSetForest import DisjointSetForest, Node
import graph3


def print_forest(DS):
    print('-'*10)
    for node in DS.forest:
        print(node.data, "->", node.parent)


def kruskal(Adj):
    T = []
    DS = DisjointSetForest()
    for k in Adj:
        DS.make_set(k)
    # print_forest(DS)
    # print("-"*10)
    
    # sort by edge weight increasing
    # converts Adj list into tuple of (weight, u, v)
    E = sorted([(w,u,v)
                for u in Adj
                for v,w in Adj[u].items()])
    print(str(E))

    for edge in E:
        print("="*10)
        print("checking edge: %s -> %s (%d)" % (edge[1], edge[2], edge[0]))
        if DS.find(edge[1]) != DS.find(edge[2]):
            T.append((edge[1],edge[2],edge[0]))
            DS.union(edge[1], edge[2])
        else:
            print("already visited this node")
        print_forest(DS)

    return T


MST = kruskal(Adj)
print("\n\n", "="*10,"\n\n")
print([(u.data,v.data,w) for u,v,w in MST])
print("Total weight:", sum([w for u,v,w in MST]))