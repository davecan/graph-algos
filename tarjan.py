# Tarjan's SCC algorithm
# adapted from https://en.wikipedia.org/wiki/Tarjan%27s_strongly_connected_components_algorithm
class Tarjan:
    index = 0
    depth = {}
    lowlink = {}
    S = []
    components = []
    Adj = None

    def __init__(self, Adj):
        self.Adj = Adj

    def search(self):
        for v in self.Adj.keys():
            if v not in self.depth:
                self.strongconnect(v)

    def strongconnect(self, v):
        self.depth[v] = self.index
        self.lowlink[v] = self.index
        self.index += 1
        self.S.append(v)

        # consider successors of v
        for w in self.Adj[v]:
            if w not in self.depth:
                # successor not yet visited, recurse on it
                self.strongconnect(w)
                self.lowlink[v] = min(self.lowlink[v], self.lowlink[w])
            elif w in self.S:
                # successor w is in stack S and hence in current SCC
                self.lowlink[v] = min(self.lowlink[v], self.depth[w])

        # if v is a root node, pop the stack and generate an SCC
        if self.lowlink[v] == self.depth[v]:
            SCC = []
            # slightly different approach than the pseudocode on wiki
            while True:
                w = self.S.pop()
                SCC.append(w)
                if w == v:
                    break
            self.components.append(SCC)