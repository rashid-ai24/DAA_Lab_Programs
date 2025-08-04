# Ex No: 6 - IMPLEMENTATION OF DIJKSTRA’S ALGORITHM USING GREEDY TECHNIQUE

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def printSolution(self, dist):
        print("Vertex \t Distance from Source")
        for node in range(self.V):
            print(node, "\t\t", dist[node])

    def minDistance(self, dist, sptSet):
        min_val = float('inf')
        min_index = -1
        for i in range(self.V):
            if dist[i] < min_val and not sptSet[i]:
                min_val = dist[i]
                min_index = i
        return min_index

    def dijkstra(self, src):
        dist = [float('inf')] * self.V
        dist[src] = 0
        sptSet = [False] * self.V
        for _ in range(self.V):
            u = self.minDistance(dist, sptSet)
            sptSet[u] = True
            for i in range(self.V):
                if self.graph[u][i] > 0 and not sptSet[i] and dist[i] > dist[u] + self.graph[u][i]:
                    dist[i] = dist[u] + self.graph[u][i]
        self.printSolution(dist)

g = Graph(5)
g.graph = [
    [0, 1, 0, 0, 0],
    [1, 0, 2, 3, 0],
    [0, 2, 0, 1, 5],
    [0, 3, 7, 0, 1],
    [0, 0, 5, 1, 0]
]
g.dijkstra(0)
