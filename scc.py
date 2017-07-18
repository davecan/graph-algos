# Finds the strongly-connected components of the graph using Tarjan's algorithm.

from tarjan import Tarjan
import graph1

tarjan = Tarjan(graph1.Adj)
tarjan.search()
print("SCC List", tarjan.components)