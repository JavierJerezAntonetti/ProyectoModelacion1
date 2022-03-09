import matplotlib.pyplot as plt
import networkx as nx
import math

def show_graph(path, graph, int2label):
    for e in graph.edges(): # Recorre todas las aristas del grafo
        graph[e[0]][e[1]]['color'] = 'grey' # Pone todas las aristas en color gris
    for i in range(len(path)-1): # Recorre todos los nodos del camino
        graph[int(path[i])][int(path[i+1])]['color'] = 'red' # Pone el nodo actual en color rojo
    edge_color_list = [graph[e[0]][e[1]]['color'] for e in graph.edges()] # Crea una lista con los colores de las aristas

    options = { # Opciones para el grafo
        "with_labels": True,
        "font_size": 10,
        "node_size": 600,
        "node_color": "skyblue",
        "edge_color": edge_color_list,
        "linewidths": 1,
        "width": 2
    }

    graph = nx.relabel_nodes(graph, int2label) # Renombra los nodos a los nombres de los destinos
    pos = nx.spring_layout(graph, k=10/math.sqrt(graph.order()), iterations=20, seed=6) # Posiciona los nodos
    nx.draw(graph, pos, **options) # Dibuja el grafo
    labels = nx.get_edge_attributes(graph,'weight') # Obtiene los pesos de las aristas
    nx.draw_networkx_edge_labels(graph,pos,edge_labels=labels) # Dibuja los pesos de las aristas
    mng = plt.get_current_fig_manager() # Obtiene el manejador de la figura
    mng.window.state("zoomed") # Maximiza la ventana
    ax = plt.gca() # Obtiene el axes de la figura
    ax.margins(0.20) # Ajusta los margenes de la figura
    plt.axis("off") # Oculta los ejes
    plt.show() # Muestra el grafo