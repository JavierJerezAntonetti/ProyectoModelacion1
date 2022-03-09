class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices # Numero de vertices
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)] # matriz de adyacencia de los vertices

    def add_edge(self, u, v, weight): # Agrega una arista al grafo
        self.edges[u][v] = weight
        self.edges[v][u] = weight