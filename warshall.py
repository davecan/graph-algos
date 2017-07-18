# Warshall's algorithm
# Converts an adjacency matrix into a reachability matrix
# by forming its reflexive-transitive closure.
# The reachability matrix contains a 1 if a path of any
# length exists between the two nodes.

def warshall(R):
    print("S  => ", R)  # starting matrix
    n = len(R)

    # makes R reflexive by marking the reflexive diagonal
    for i in range(0,n):
        R[i][i] = 1   
    
    print("R  => ", R)  # shows reflexive closure
    
    # process the triple to make the transitive closure
    for k in range(0,n):
        for i in range(0,n):
            for j in range(0,n):
                R[i][j] = R[i][j] | (R[i][k] & R[k][j])
        print(k, " => ", R)  # matrix for each k
    return R

if __name__ == "__main__":
    import graph4
    
    R = warshall(graph4.Adj)
    print(R)