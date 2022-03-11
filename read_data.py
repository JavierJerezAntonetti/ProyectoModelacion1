import os,sys

# Inicializamos los diccionarios vacios
edge_list = []
vertices = {}
int2label = {}
label2int = {}
visas = {}
nombres = {}

with open(os.path.join(sys.path[0], 'destinos.txt'), "r") as destinos: # Abre el archivo destinos.txt
    destinos = destinos.read().splitlines() # Separa las lineas del archivo
    for i in destinos: # Recorre todas las lineas del archivo
        num,destino = i.split(":") # Separa el numero de vertice y los datos del vertice
        vertices[destino.split(",")[0]] = int(num) # Agrega el numero de vertice y el nombre del vertice al diccionario vertices
        int2label[int(num)] = destino.split(",")[0] # Agrega el numero de vertice y el nombre del vertice al diccionario int2label
        label2int[destino.split(",")[0]] = int(num) # Agrega el numero de vertice y el nombre del vertice al diccionario label2int
        nombres[int(num)] = destino.split(",")[1] # Agrega el nombre completo del vertice al diccionario nombres
        visas[int(num)] = destino.split(",")[2] # Agrega el numero de vertice y un booleano indicando si tiene visa

with open(os.path.join(sys.path[0], 'tarifas.txt'), "r") as tarifas: # Abre el archivo tarifas.txt
    next(tarifas) # Salta la primera linea
    tarifas = tarifas.read().splitlines() # Separa las lineas del archivo
    for i in tarifas: # Recorre todas las lineas del archivo
        data = i.split(",") # Separa los datos de la linea
        source = vertices[data[0]] # Obtiene el numero de vertice del origen
        target = vertices[data[1]] # Obtiene el numero de vertice del destino
        weight = int(data[2]) # Obtiene el peso de la arista
        edge_list.append([source, target, weight]) # Agregamos los datos a la lista de aristas