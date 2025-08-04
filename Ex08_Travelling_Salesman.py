# Ex No: 8 - IMPLEMENTATION OF TRAVELLING SALESMAN PROBLEM USING BRANCH AND BOUND

import numpy as np
from sys import maxsize
from itertools import permutations

def TSProblem(graph, s):
    vertex = [i for i in range(len(graph)) if i != s]
    min_path = maxsize
    for i in permutations(vertex):
        current_pathweight = 0
        k = s
        for j in i:
            current_pathweight += graph[k][j]
            k = j
        current_pathweight += graph[k][s]
        min_path = min(min_path, current_pathweight)
    return min_path

V = int(input("Enter the number of cities: "))
print("Enter the cost matrix:")
matrix = [[int(input()) for _ in range(V)] for _ in range(V)]
matrix = np.array(matrix).reshape(V, V)
print("The Cost Matrix is\n", matrix)
s = 0
cost = TSProblem(matrix, s)
print("Travelling Salesman Cost is:", cost)
