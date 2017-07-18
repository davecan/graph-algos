# stack-based depth-first search
# adapted from CLRS
# adds stack to implement SCC algorithm
class DFS:
    color = {}
    parent = {}
    start_time = {}
    end_time = {}
    tree_edges = []
    forward_edges = []
    back_edges = []
    cross_edges = []
    stack = []
    Adj = None
    time = 0

    def __init__(self, Adj):
        self.Adj = Adj

    def search(self, node = None):
        # init -- probably not needed, could just check not exists instead of checking color == W
        for u in self.Adj:   
            self.color[u] = 'W'
            self.parent[u] = None
        # if a node is specified only process it, otherwise sweep all of them
        if node:
            self.__visit(node)
        else:
            for u in self.Adj:
                if self.color[u] == 'W':
                    self.__visit(u)

    def __visit(self, u):
        self.time += 1
        self.start_time[u] = self.time
        self.color[u] = 'G'
        for v in self.Adj[u]:
            if self.color[v] == 'W':
                self.tree_edges.append((u,v))
                self.parent[v] = u
                self.__visit(v)
        self.color[u] == 'B'
        self.time += 1
        self.end_time[u] = self.time
        self.stack.append(u)

    def classify_edges(self):
        for u in self.Adj:
            for v in self.Adj[u]:
                if self.start_time[u] > self.start_time[v] and self.end_time[u] < self.end_time[v]:
                    self.back_edges.append((u,v))
                elif (self.start_time[u] < self.start_time[v] and self.end_time[u] < self.end_time[v]) or (self.start_time[u] > self.start_time[v] and self.end_time[u] > self.end_time[v]):
                    self.cross_edges.append((u,v))
                elif self.start_time[u] < self.start_time[v] and self.end_time[u] > self.end_time[v] and (u,v) not in self.tree_edges:
                    self.forward_edges.append((u,v))

    # returns dict containing:
    #    key = node
    #    val = (start time, end time)
    def times(self):
        d = {n:None for n in self.parent}
        for n in d:
            d[n] = (self.start_time.get(n), self.end_time.get(n))
        return d   

    def is_back_edge(self, u, v):
        return self.start_time[u] > self.start_time[v] and self.end_time[v] < self.end_time[u]

    def is_cross_edge(self, u, v):
        return self.start_time[v] < self.start_time[u] and self.end_time[v] < self.end_time[u]

    def is_forward_edge(self, u, v):
        return self.start_time[u] < self.start_time[v] and self.end_time[u] > self.end_time[v] and (u,v) not in self.tree_edges
