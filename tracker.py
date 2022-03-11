def track_path(source, target, pred):
    path = [target] # Crea una lista PATH inicializada con el target
    while path[0] != source: # Mientras el primer elemento de la lista no sea el source
        if pred[path[0]] != None: # Si el predecesor del primer elemento de la lista no es None
            path.insert(0, pred[path[0]]) # Insertamos el predecesor del primer elemento de la lista al principio deL path
    return path # Retornamos el path
