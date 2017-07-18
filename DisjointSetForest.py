class Node():
    def __init__(self, data, parent = None):
        self.data = data
        self.parent = self
        self.child = self
        self.rank = 0

    def __hash__(self):
        return hash(self.data)

    def __str__(self):
        return self.data

    # support total ordering
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.data == other.data
        return False

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.data < other.data

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)


class DisjointSetForest():
    def __init__(self):
        self.forest = []

    def make_set(self, node):
        if node not in self.forest:
            self.forest.append(node)
            return node
        raise self.forest

    def find(self, node):
        if node.parent != node:
            node.parent = self.find(node.parent)
            node.parent.child = node
        return node.parent

    def union(self, node_x, node_y):
        print("union {}, {}".format(node_x,node_y))
        xroot = self.find(node_x)
        yroot = self.find(node_y)
        if xroot == yroot:
            return
        if xroot.rank < yroot.rank:
            xroot.parent = yroot
            yroot.child = xroot
        elif xroot.rank > yroot.rank:
            yroot.parent = xroot
            xroot.child = yroot
        else:
            yroot.parent = xroot
            xroot.child = yroot
            xroot.rank = xroot.rank + 1

    def roots(self):
        return [n for n in DS.forest if n.parent == n]



if __name__ == "__main__":

    def print_inverted_tree(node, depth=0):
        print("  "*depth, "--", node.data)
        if node.parent != node:
            print_inverted_tree(node.parent, depth+1)

    def print_forest(DS):
        for node in DS.forest:
            print(node.data, "->", node.parent)
        print('-'*10)

    def print_roots(DS):
        print("ROOTS: ", ' '.join([n.data for n in DS.roots()]))


    # Uses the Disjoint Set Forest to manually walk through the graph of Kruskal's algo from CLRS step by step
    # showing how the data structure performs the union-find process at each step.

    A = Node("a")
    B = Node("b")
    C = Node("c")
    D = Node("d")
    E = Node("e")
    F = Node("f")
    G = Node("g")

    DS = DisjointSetForest()
    for node in [A,B,C,D,E,F,G]:
        DS.make_set(node)

    # now walk through the diagram one step at a time

    # step 0 - initial state
    print_roots(DS)
    print_forest(DS)

    # step 1
    print_roots(DS)
    DS.union(C,F)
    print_forest(DS)

    # step 2
    print_roots(DS)
    DS.union(C,D)
    print_forest(DS)

    # step 3
    print_roots(DS)
    DS.union(F,G)
    print_forest(DS)

    # step 4
    print_roots(DS)
    DS.union(A,B)
    print_forest(DS)

    # step 5
    print_roots(DS)
    DS.union(F,E)
    print_forest(DS)

    # step 6
    print_roots(DS)
    DS.union(A,C)
    print_forest(DS)
