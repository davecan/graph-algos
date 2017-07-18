# breadth-first search
# given adjacency list, generates BFS tree
# adapted from MIT OCW
class BFS:
    Adj = None
    __pp_tree = {}

    def __init__(self, Adj):
        self.Adj = Adj

    def search(self, s):
        level = {s:0}
        parent = {s:None}
        i = 1
        frontier = [s]
        while frontier:
            next = []
            for u in frontier:
                if u in self.Adj:
                    for v in self.Adj[u]:
                        if v not in level:
                            level[v] = i
                            parent[v] = u
                            next.append(v)
            frontier = next
            i += 1
        self.__pp_tree = parent

    def tree(self):
        d = {}
        for u,v in self.__pp_tree.items():
            if v not in d:
                d[v] = [u]
            if u not in d[v]: 
                d[v].append(u)
        d.pop(None)  # remove null pointer to first node
        return d


if __name__ == '__main__':
    import graph1

    bfs = BFS(graph1.Adj)
    bfs.search("A")
    print(bfs.tree())