import time
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

matrix = np.loadtxt('matrix')

def internal_bellman_ford(matrix, source, target):
    graph = nx.DiGraph(matrix)
    position = nx.circular_layout(graph)
    labels = nx.get_edge_attributes(graph, 'weight')
    start_time = time.time()
    bl_path = nx.bellman_ford_path(graph, source, target)
    bl_length = nx.bellman_ford_path_length(graph, source, target)
    end_time = time.time() - start_time
    print("Internal path length: ", bl_length)
    print("Search time of internal method: ",end_time)
    node_colors = ["red" if n in bl_path else "blue" for n in graph.nodes()]
    nx.draw_networkx_nodes(graph, position, node_color = node_colors,  with_labels = False)
    nx.draw_networkx_labels(graph, position)
    nx.draw_networkx_edges(graph, position, edge_labels = False)
    nx.draw_networkx_edge_labels(graph, position, edge_labels = labels)
    plt.show()

class Graph:
    def __init__(self, number_of_vertices):
        self.V = number_of_vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def my_bellman_ford(self, source, target):
        distance = [float("Inf")] * self.V
        distance[source] = 0
        start_time = time.time()
        for i in range(self.V - 1):
            for u, v, w in self.graph:
                if distance[u] != float("Inf") and distance[u] + w < distance[v]:
                    distance[v] = distance[u] + w
        end_time = time.time() - start_time
        print("My path length: ", distance[target])
        print("Search time of my method: ", end_time)

def main():
    print("Input source vertex: ")
    source = int (input())
    print("Input target vertex: ")
    target = int (input())

    # testing my function
    n = np.shape(matrix)[0]
    graph = Graph(n)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != 0:
                graph.addEdge(i, j, matrix[i][j])
    graph.my_bellman_ford(source, target)

    # testing internal function
    internal_bellman_ford(matrix, source, target)

main()