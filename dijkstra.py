from queue import PriorityQueue
from read_data import visas

def dijkstra(graph, start_vertex, tiene_visa): # start_vertex es el nodo inicial, tiene_visa es un booleano que indica si el viajero tiene visa o no
    shortest_paths = {v:float('inf') for v in range(graph.v)} # Inicializamos la distancia hacia cada nodo a infinito
    pred = {i:None for i in range(graph.v)} # Inicializamos el predecesor de cada nodo a None
    visited = {n:False for n in range(graph.v)} # Inicializamos la lista de visitados a 0 en cada vertice
    shortest_paths[start_vertex] = 0 # El nodo inicial tiene distancia 0

    pq = PriorityQueue() # Inicializamos una cola de prioridad para ordenar rapidamente los nodos por distancia
    pq.put((0, start_vertex)) # Colocamos el nodo inicial en la cola de prioridad

    while not pq.empty(): # Mientras la cola no este vacia
        (dist, current_vertex) = pq.get() # Obtenemos el nodo con mayor prioridad en la cola, que es el de menor distancia
        visited[current_vertex] = True # Colocamos el nodo como visitado
        for neighbor in range(graph.v): # Para cada nodo vecino
            queued = False # Inicializamos el asistente que revisara si el nodo ya esta encolado
            if graph.edges[current_vertex][neighbor] != -1 and current_vertex != neighbor: # Si existe una arista entre el nodo actual y el vecino

                if not tiene_visa and visas[neighbor] == "True": # Si el viajero no tiene visa y el nodo vecino si la requiere
                    continue # No se puede llegar a ese nodo, lo saltamos y continuamos con el siguiente nodo vecino
                
                if not visited[neighbor]: # Si el vecino no ha sido visitado
                    distance = graph.edges[current_vertex][neighbor] # Obtenemos la distancia entre el nodo actual y el vecino
                    old_cost = shortest_paths[neighbor] # Obtenemos la vieja distancia hacia el vecino
                    new_cost = shortest_paths[current_vertex] + distance # Calculamos la nueva distancia hacia el vecino

                    if new_cost < old_cost: # Si la nueva distancia es menor que la vieja
                        for i in pq.queue: # Para cada nodo en la cola de prioridad
                            if neighbor == i[-1]: # Si el nodo vecino esta en la cola de prioridad
                                queued = True # Colocamos el asistente en True

                        if not queued: # Si el asistente esta en False
                            pq.put((new_cost, neighbor)) # Colocamos el vecino en la cola de prioridad
                        shortest_paths[neighbor] = new_cost # Actualizamos la distancia hacia el vecino
                        pred[neighbor] = current_vertex # Actualizamos el predecesor del vecino
                        
    return shortest_paths,pred # Retornamos las distancias hacia cada nodo y el predecesor