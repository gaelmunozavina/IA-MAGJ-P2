import heapq

def busqueda_voraz(grafo, inicio, meta, heuristica):
    """
    Realiza una búsqueda voraz primero el mejor.
    
    Args:
        grafo: Diccionario de adyacencia {nodo: [vecinos]}.
        inicio: Nodo de partida.
        meta: Nodo objetivo.
        heuristica: Diccionario con los valores estimados h(n) hasta la meta.
    """
    # Cola de prioridad: (valor_heuristico, nodo_actual, camino_recorrido)
    frontera = [(heuristica[inicio], inicio, [inicio])]
    visitados = set()

    print(f"Iniciando búsqueda voraz hacia: {meta}")

    while frontera:
        # Extraemos el nodo que "parece" estar más cerca de la meta
        h_val, nodo_actual, camino = heapq.heappop(frontera)

        if nodo_actual == meta:
            return camino, h_val

        if nodo_actual not in visitados:
            print(f"Visitando: {nodo_actual} (h={h_val})")
            visitados.add(nodo_actual)

            for vecino in grafo.get(nodo_actual, []):
                if vecino not in visitados:
                    # Solo nos importa la heurística del vecino
                    nuevo_camino = camino + [vecino]
                    heapq.heappush(frontera, (heuristica[vecino], vecino, nuevo_camino))

    return None, float('inf')

# --- EJEMPLO DE PRUEBA ---
# Mapa de conexiones
conexiones = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [], 'E': [], 'F': ['G'], 'G': []
}

# Valores de h(n) - Distancia estimada en línea recta a 'G'
tabla_heuristica = {
    'A': 6, 'B': 5, 'C': 2, 'D': 7, 'E': 4, 'F': 1, 'G': 0
}

ruta, costo = busqueda_voraz(conexiones, 'A', 'G', tabla_heuristica)

if ruta:
    print(f"\nCamino encontrado: {' -> '.join(ruta)}")
else:
    print("\nNo se encontró la meta.")
