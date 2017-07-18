from tarjan import Tarjan
from warshall import warshall


# Defines a partial order on the condensation graph.
# Uses Tarjan to find the strongly connected components. (the condensation graph)
# Then uses Warshall to form reflexive-transitive closure.
# Once we have the closure, ordering the closure will suffice
# to order to graph, since nodes in the components are all equivalent.
def partial_order(Adj, legend):

    #======================================================
    # find the strongly connected components
    # using the Tarjan algorithm
    #
    # HACK -- this Tarjan implementation requires an adjacency list
    # but this input is an adjacency matrix, so we have to convert
    # the matrix to a list to feed it into Tarjan.
    # In a real implementation we would have a Tarjan that accepts
    # a matrix here instead, so no conversion would be needed.
    #======================================================

    # build the adjacency list to use with Tarjan
    # by scanning the adjacency matrix and converting it
    adjlist = {}

    # conversion is a bit tricky...
    for i in range(0,len(Adj)):
        adjlist[legend[i]] = []
        for j in range(0,len(Adj[i])):
            if Adj[i][j] != 0:
                adjlist[legend[i]].append(legend[j])

    # get the SCCs
    tarjan = Tarjan(adjlist)
    tarjan.search()
    SCC = tarjan.components

    #======================================================
    # build the SCC adjacency matrix by scanning the
    # original adjacency matrix and appending an edge
    # between components if an edge exists between
    # individual component nodes in the original matrix
    #======================================================

    # initialize the SCC adjacency matrix
    SCC_Adj = []
    for i in range(0,len(SCC)):
        SCC_Adj.append([])
        for j in range(0,len(SCC)):
            SCC_Adj[i].append(0)

    # this brute-force method works! but is something like O(n^4)
    for CC in SCC:                                      # check for edges from this component to the others
        for i in range(0,len(CC)):                      # pick a node from the "from" component to check
            row = legend.index(CC[i])                   # "row" is the row in the adjacency matrix for the "from" node
            for CC2 in [x for x in SCC if x != CC]:     # check for edges to the other connected components
                for j in range(0,len(CC2)):             # CC2 is the "to" component to check
                    col = legend.index(CC2[j])          # "col" is the col in the adjacency matrix for the "to" node
                    if Adj[row][col] != 0:
                        # edge exists from node in CC1 to node in CC2
                        # get index of CC1 and CC2 and update the
                        # SCC adjacency matrix to reflect the edge
                        row_cc_index = [i for i,cc in enumerate(SCC) if legend[row] in cc][0]  # "from" CC1
                        col_cc_index = [i for i,cc in enumerate(SCC) if legend[col] in cc][0]  # "to" CC2
                        SCC_Adj[row_cc_index][col_cc_index] = Adj[row][col]
    print(SCC)
    print(SCC_Adj)

    #======================================================
    # form the reflexive-transitive closure of the SCC
    # adjacency matrix aka its reachability matrix which
    # defines a partial order on the connected components
    #
    # since the nodes in a connected component are by
    # definition bi-connected they are "equal" in a partial
    # order, so the SCC ordering will suffice to establish
    # a partial order on the graph as a whole
    #
    # uses Warshall's algorithm to form the closure
    #======================================================

    return warshall(SCC_Adj)


if __name__ == "__main__":
    
    import graph4
    legend = ["A","B","C","D","E"]

    R = partial_order(graph4.Adj, legend)
    print("*"*10)
    print(R)