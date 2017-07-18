# Floyd's algorithm
# Converts an adjacency matrix into a reachability matrix
# by forming its reflexive-transitive closure.
# The reachability matrix contains a 1 if a path of any
# length exists between the two nodes.
# Differs from Warshall's algorithm in that it also
# provides the length of every path.

import sys

def floyd(R):
    n = len(R)
    # initialize all non-trivial edges to infinity
    for i in range(0,n):
        for j in range(0,n):
            if i == j:
                R[i][j] = 0
            elif R[i][j] == 0:
                R[i][j] = sys.maxsize  # "infinity"

    # process the triple
    for k in range(0,n):
        for i in range(0,n):
            for j in range(0,n):
                R[i][j] = min(R[i][j], R[i][k] + R[k][j])
        print(k, " => ", R)  # matrix for each k    
    return R



if __name__ == "__main__":
    import graph4

    R = floyd(graph4.Adj)

    for r in R:
        print(r)