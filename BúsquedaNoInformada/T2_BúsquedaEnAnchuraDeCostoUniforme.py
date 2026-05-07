import heapq

def busqueda_costo_uniforme(grafo, inicio, meta):
    """
    Encuentra la ruta con el menor costo acumulado entre un inicio y una meta.
    
    Argumentos:
        grafo: Diccionario donde las llaves son nodos y los valores son listas 
               de tuplas (vecino, costo).
        inicio: Nodo de partida.
        meta: Nodo objetivo.
    """
    
    # 1. Cola de prioridad (priority queue)
    # Formato: (costo_acumulado, nodo_actual, camino_recorrido)
    # heapq siempre mantiene el elemento con menor costo al principio.
    prioridad_cola = [(0, inicio, [inicio])]
    
    # 2. Diccionario para guardar el costo mínimo visitado a cada nodo
    visitados = {}

    while prioridad_cola:
        # Extraemos el nodo con el menor costo acumulado hasta el momento
        (costo, nodo_actual, camino) = heapq.heappop(prioridad_cola)

        # Si llegamos a la meta, devolvemos el resultado porque UCS garantiza
        # que la primera vez que la meta sale de la cola, es por el camino más barato.
        if nodo_actual == meta:
            return camino, costo

        # Si no hemos visitado el nodo o encontramos un camino más barato
        if nodo_actual not in visitados or costo < visitados[nodo_actual]:
            visitados[nodo_actual] = costo
            
            # Explorar vecinos
            for (vecino, costo_arista) in grafo.get(nodo_actual, []):
                nuevo_costo = costo + costo_arista
                nuevo_camino = camino + [vecino]
                heapq.heappush(prioridad_cola, (nuevo_costo, vecino, nuevo_camino))

    return None, float('inf')

# --- CONFIGURACIÓN DEL GRAFO (Ejemplo de prueba) ---
# Los valores representan el costo (distancia, tiempo, dinero, etc.)
mapa_conexiones = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

# --- EJECUCIÓN ---
inicio_test = 'A'
meta_test = 'D'

ruta, costo_total = busqueda_costo_uniforme(mapa_conexiones, inicio_test, meta_test)

if ruta:
    print(f"La ruta más barata es: {' -> '.join(ruta)}")
    print(f"Costo total acumulado: {costo_total}")
else:
    print("No se encontró un camino a la meta.")
