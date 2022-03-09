from queue import Queue

def minEdgeBFS(graph, start_vertex): # u es el nodo inicial, v es el nodo final
    pred = {i:None for i in range(graph.v)} # Inicializamos el predecesor de cada nodo a None
    visited = {n:False for n in range(graph.v)} # Inicializamos la lista de visitados a False en cada vertice
    minimun_edges = {v:float("inf") for v in range(graph.v)} # Inicializamos la distancia hacia cada nodo a infinito

    Q = Queue() # Inicializamos una cola
    minimun_edges[start_vertex] = 0 # El nodo inicial tiene distancia 0
    Q.put(start_vertex) # Colocamos el nodo inicial en la cola
    visited[start_vertex] = True # Marcamos el nodo inicial como visitado
    while not Q.empty(): # Mientras la cola no este vacia
        current_vertex = Q.get() # Obtenemos el nodo con mayor prioridad en la cola
        for neighbor in range(graph.v): # Para cada nodo vecino
            if graph.edges[current_vertex][neighbor] != -1 and visited[neighbor] == False: # Si existe una arista entre el nodo actual y el vecino y el vecino no ha sido visitado
                pred[neighbor] = current_vertex # Actualizamos el predecesor del vecino
                minimun_edges[neighbor] = minimun_edges[current_vertex] + 1 # Actualizamos la distancia hacia el vecino
                Q.put(neighbor) # Colocamos el vecino en la cola
                visited[neighbor] = True # Marcamos el vecino como visitado

    return minimun_edges,pred # Retornamos las distancias hacia cada nodo y el predecesor