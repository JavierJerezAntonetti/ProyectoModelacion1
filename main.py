import os
from graph import Graph
from dijkstra import dijkstra
from bfs import minEdgeBFS
from tracker import track_path
from show_graph import show_graph
from read_data import edge_list, vertices, int2label, visas, nombres

# Revisa si el usuario tiene las dependencias instaladas y si no las instala
try:
    import networkx as nx
    from texttable import Texttable
    from colorama import Fore
except ImportError:
    os.system("pip install networkx")
    os.system("pip install texttable")
    os.system("pip install colorama")
    import networkx as nx
    from texttable import Texttable
    from colorama import Fore

def clear(): # Limpia la consola
    if os.name == 'nt': #para windows
        _ = os.system('cls')
    else: #para mac y linux
        _ = os.system('clear')

max_vertices = len(vertices) # Obtiene el numero de vertices del grafo

#print(np.array(edge_list)) # Imprime la lista de vertices bonita

graph = Graph(max_vertices) # Crea el grafo con la cantidad de vertices
for i in range(len(edge_list)): # Recorre todas las aristas
    graph.add_edge(edge_list[i][0], edge_list[i][1], int(edge_list[i][2])) # Construye el grafo con los vertices y aristas

G = nx.Graph() # Crea un grafo con la libreria networkx, este es para mostrar el grafo en pantalla

for i in range(graph.v): # Recorre todas las filas de la matriz del grafo original
    for j in range(graph.v): # Recorre todas las columnas de la matriz del grafo original
        if graph.edges[i][j] != -1: # Si existe una arista entre los vertices
            G.add_edge(i,j,weight=graph.edges[i][j])  # Agrega la arista al grafo con la libreria networkx


xy_axis = [['Numero', 'Ciudad']] # Creamos el titulo de la tabla
for i in int2label: # Recorremos el diccionario int2label para obtener los nombres de los vertices
    xy_axis.append([i, int2label[i]]) # Agregamos los vertices y sus nombres a la tabla

def print_cities(): # Imprime la tabla con los nombres de los vertices
    t = Texttable()
    t.add_rows(xy_axis)
    print(t.draw())

# Le pedimos al usuario que seleccione si tiene visa o no
while True:
    print("\nSelecciona si tienes visa o no\n\n1) Si tengo\n\n2) No tengo")
    try:
        visa = int(input("\nVisa: "))
        if visa == 1:
            tiene_visa = True
            clear()
            break
        elif visa == 2:
            tiene_visa = False
            clear()
            break
        else:
            clear()
            print("\n" + Fore.RED + "Ingrese una opción válida" + Fore.RESET)
            continue
    except ValueError:
        clear()
        print("\n" + Fore.RED + "Ingrese un valor numérico" + Fore.RESET)
        continue

# Le pedimos al usuario que seleccione la ciudad de origen
while True:
    print_cities()
    print("\nSelecciona el numero de la ciudad de origen" + Fore.RESET)
    try:
        origen = int(input("\nOrigen: "))
        if origen >= 0 and origen < max_vertices: # Si el numero de vertice es valido salimos del ciclo
            clear()
            break
        else:
            clear()
            print("\n" + Fore.RED + "Ingrese una opción válida" + Fore.RESET)
            continue
    except ValueError:
        clear()
        print("\n" + Fore.RED + "Ingrese un valor numérico" + Fore.RESET)
        continue

print(f"\nSelección de origen: {nombres[origen]}\n")

# Le pedimos al usuario que seleccione la ciudad de destino
while True:
    print_cities()
    print("\nSelecciona el numero de la ciudad de destino")
    try:
        destino = int(input("\nDestino: "))
        if destino >= 0 and destino < max_vertices: # Si el numero de vertice es valido
            if origen == destino: # Si el numero de vertice es igual al de origen no puede viajar a la misma ciudad, pedimos una nueva ciudad
                clear()
                print("\n" + Fore.RED + "No puede viajar a la misma ciudad" + Fore.RESET)
                continue
            clear()
            break
        else:
            clear()
            print("\n" + Fore.RED + "Ingrese una opción válida" + Fore.RESET)
            continue
    except ValueError:
        clear()
        print("\n" + Fore.RED + "Ingrese un valor numérico" + Fore.RESET)
        continue

print(f"\nSelección de destino: {nombres[destino]}\n")

# Le pedimos al usuario que seleccione el tipo de ruta
while True:
    print("\nSelecciona el tipo de ruta que deseas\n\n1) Mas barata\n\n2) Menos segmentos de vuelo")
    try:
        ruta = int(input("\nRuta: "))
        if ruta == 1 or ruta == 2: # Si el numero de ruta es valido salimos del ciclo
            clear()
            break
        else:
            clear()
            print("\n" + Fore.RED + "Ingrese una opción válida" + Fore.RESET)
            continue
    except ValueError:
        clear()
        print("\n" + Fore.RED + "Ingrese un valor numérico" + Fore.RESET)
        continue


if ruta == 1: # Si el usuario eligio la ruta mas barata
    if tiene_visa == False and visas[destino] == "True": # Si el usuario no tiene visa y la ciudad de destino requiere visa
        print("\n" + Fore.RED + f"{nombres[destino]} requiere visa, por lo que no es posible que usted viaje a ella" + Fore.RESET) # Imprimimos que no es posible viajar a la ciudad de destino
        exit() # Salimos del programa
    shortest_paths,pred_dijkstra = dijkstra(graph, origen, tiene_visa) # Obtenemos los caminos mas baratos y los predecesores
    path = track_path(origen, destino, pred_dijkstra) # Obtenemos el camino mas barato entre los vertices de origen y destino mediante los predecesores
    show_graph(path, G, int2label) # Mostramos el grafo con el camino mas barato
    count = 0 # Contador ayudante
    for i in path: # Recorremos el camino mas barato
        path[count] = int2label[i] # Cambiamos los vertices por sus nombres
        count += 1 # Aumentamos el contador ayudante
    print(f"\nLa ruta mas barata es: {path}") # Imprimimos el camino mas barato

elif ruta == 2: # Si el usuario eligio la ruta menos segmentos de vuelo
    if tiene_visa == False and visas[destino] == "True": # Si el usuario no tiene visa y la ciudad de destino requiere visa
        print("\n" + Fore.RED + f"{nombres[destino]} requiere visa, por lo que no es posible que usted viaje a ella" + Fore.RESET) # Imprimimos que no es posible viajar a la ciudad de destino
        exit() # Salimos del programa
    min_edges,pred_bfs = minEdgeBFS(graph, origen, tiene_visa) # Obtenemos los caminos menos segmentos de vuelo y los predecesores
    path = track_path(origen, destino, pred_bfs) # Obtenemos el camino menos segmentos de vuelo entre los vertices de origen y destino mediante los predecesores
    show_graph(path, G, int2label) # Mostramos el grafo con el camino menos segmentos de vuelo
    count = 0 # Contador ayudante
    for i in path: # Recorremos el camino menos segmentos de vuelo
        path[count] = int2label[i] # Cambiamos los vertices por sus nombres
        count += 1 # Aumentamos el contador ayudante
    print(f"\nLa ruta con menos segmentos es: {path}") # Imprimimos el camino menos segmentos de vuelo