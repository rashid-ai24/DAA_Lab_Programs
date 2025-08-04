# Ex No: 5 - IMPLEMENTATION OF WARSHALL’S AND FLOYD'S ALGORITHMS USING DYNAMIC PROGRAMMING METHOD

nv = 4
INF = 999

def floyd(G):
    dist = [list(row) for row in G]
    for k in range(nv):
        for i in range(nv):
            for j in range(nv):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    display(dist)

def display(dist):
    print("Shortest distance between every pair of vertices")
    for i in range(nv):
        for j in range(nv):
            print("INF" if dist[i][j] == INF else dist[i][j], end="  ")
        print()

G = [
    [0, 5, INF, 3],
    [50, 0, 15, 5],
    [30, INF, 0, 15],
    [15, INF, 5, 0]
]
floyd(G)
