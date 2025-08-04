# Ex No: 3 - IMPLEMENTATION OF TOPOLOGICAL SORTING USING DECREASE AND CONQUER TECHNIQUE

from collections import defaultdict

class Graph:
    def __init__(self, directed=False):
        self.graph = defaultdict(list)
        self.directed = directed

    def Edge(self, frm, to):
        self.graph[frm].append(to)
        if not self.directed:
            self.graph[to].append(frm)

    def visit(self, s, visited, sortlist):
        visited[s] = True
        for i in self.graph[s]:
            if not visited[i]:
                self.visit(i, visited, sortlist)
        sortlist.insert(0, s)

    def topological_Sort(self):
        visited = {i: False for i in self.graph}
        sortlist = []
        for v in self.graph:
            if not visited[v]:
                self.visit(v, visited, sortlist)
        print(sortlist)

g = Graph(directed=True)
g.Edge(1, 2)
g.Edge(1, 3)
g.Edge(3, 4)
g.Edge(4, 5)
g.Edge(5, 6)
g.Edge(6, 7)
g.Edge(7, 8)
print("The Result after Topological Sort:")
g.topological_Sort()
