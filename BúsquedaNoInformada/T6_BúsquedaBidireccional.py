from collections import deque

def busqueda_bidireccional(grafo, inicio, meta):
    """
    Realiza una búsqueda bidireccional para encontrar el camino entre inicio y meta.
    
    Args:
        grafo: Diccionario de adyacencia.
        inicio: Nodo de partida.
        meta: Nodo objetivo.
    """
    if inicio == meta:
        return [inicio]

    # Colas para las dos búsquedas (Hacia adelante y Hacia atrás)
    cola_inicio = deque([inicio])
    cola_meta = deque([meta])

    # Diccionarios para rastrear el camino y marcar visitados
    # Guardan {nodo_visitado: nodo_padre} para reconstruir la ruta
    visitados_inicio = {inicio: None}
    visitados_meta = {meta: None}

    while cola_inicio and cola_meta:
        # 1. Expandir un paso desde el inicio
        resultado = expandir_nivel(grafo, cola_inicio, visitados_inicio, visitados_meta)
        if resultado:
            return reconstruir_camino(resultado, visitados_inicio, visitados_meta)

        # 2. Expandir un paso desde la meta
        resultado = expandir_nivel(grafo, cola_meta, visitados_meta, visitados_inicio)
        if resultado:
            return reconstruir_camino(resultado, visitados_inicio, visitados_meta)

    return None

def expandir_nivel(grafo, cola, mis_visitados, otros_visitados):
    """ Función auxiliar para avanzar un nivel en la búsqueda """
    nodo = cola.popleft()
    for vecino in grafo.get(nodo, []):
        if vecino not in mis_visitados:
            mis_visitados[vecino] = nodo
            cola.append(vecino)
            # ¡Intersección encontrada! El vecino ya fue visitado por la otra búsqueda
            if vecino in otros_visitados:
                return vecino
    return None

def reconstruir_camino(nodo_interseccion, visitados_inicio, visitados_meta):
    """ Une los caminos de ambas búsquedas para formar la ruta final """
    camino = []
    
    # Parte 1: Desde el inicio hasta el punto de encuentro
    temp = nodo_interseccion
    while temp is not None:
        camino.append(temp)
        temp = visitados_inicio[temp]
    camino.reverse()
    
    # Parte 2: Desde el punto de encuentro hasta la meta
    temp = visitados_meta[nodo_interseccion]
    while temp is not None:
        camino.append(temp)
        temp = visitados_meta[temp]
        
    return camino

# --- EJEMPLO DE PRUEBA ---
red_conexiones = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B', 'F'],
    'E': ['C', 'F'],
    'F': ['D', 'E']
}

ruta = busqueda_bidireccional(red_conexiones, 'A', 'F')

if ruta:
    print(f"Ruta encontrada por intersección: {' -> '.join(ruta)}")
else:
    print("No se encontró conexión entre los puntos.")

