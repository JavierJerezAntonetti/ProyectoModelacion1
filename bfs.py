from queue import Queue
from read_data import visas

def minEdgeBFS(graph, start_vertex, tiene_visa): # start_vertex es el nodo inicial, tiene_visa es un booleano que indica si el viajero tiene visa o no
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
            if graph.edges[current_vertex][neighbor] != -1 and current_vertex != neighbor: # Si existe una arista entre el nodo actual y el vecino y el nodo actual no es el vecino
                
                if not tiene_visa and visas[neighbor] == "True": # Si el viajero no tiene visa y el nodo vecino si la requiere
                    continue # No se puede llegar a ese nodo, lo saltamos y continuamos con el siguiente nodo vecino
                
                if not visited[neighbor]: # Si el vecino no ha sido visitado
                    pred[neighbor] = current_vertex # Actualizamos el predecesor del vecino
                    minimun_edges[neighbor] = minimun_edges[current_vertex] + 1 # Actualizamos la distancia hacia el vecino
                    Q.put(neighbor) # Colocamos el vecino en la cola
                    visited[neighbor] = True # Marcamos el vecino como visitado

    return minimun_edges,pred # Retornamos las distancias hacia cada nodo y el predecesor