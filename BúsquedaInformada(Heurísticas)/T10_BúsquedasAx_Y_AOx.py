import heapq

def busqueda_a_estrella(grafo, inicio, meta, heuristica):
    """
    Realiza una búsqueda A* para encontrar el camino óptimo.
    
    Args:
        grafo: Diccionario {nodo: [(vecino, costo_real)]}.
        inicio: Nodo de partida.
        meta: Nodo objetivo.
        heuristica: Diccionario con los valores h(n).
    """
    # Cola de prioridad: (f_total, costo_g, nodo_actual, camino)
    # f_total = costo_g + heuristica[nodo_actual]
    frontera = [(heuristica[inicio], 0, inicio, [inicio])]
    
    # Diccionario para registrar el mejor costo g encontrado para cada nodo
    visitados = {inicio: 0}

    print(f"--- Iniciando A* hacia {meta} ---")

    while frontera:
        # Extraemos el nodo con el menor f(n) total
        f, g, nodo_actual, camino = heapq.heappop(frontera)

        if nodo_actual == meta:
            return camino, g

        # Explorar vecinos
        for vecino, costo_arista in grafo.get(nodo_actual, []):
            nuevo_costo_g = g + costo_arista
            
            # Si encontramos un camino nuevo o más corto hacia el vecino
            if vecino not in visitados or nuevo_costo_g < visitados[vecino]:
                visitados[vecino] = nuevo_costo_g
                f_total = nuevo_costo_g + heuristica.get(vecino, 0)
                nuevo_camino = camino + [vecino]
                heapq.heappush(frontera, (f_total, nuevo_costo_g, vecino, nuevo_camino))
                print(f"  Añadiendo {vecino}: g={nuevo_costo_g}, h={heuristica.get(vecino,0)}, f={f_total}")

    return None, float('inf')

# --- CONFIGURACIÓN DE PRUEBA ---
# Grafo con costos reales: (vecino, costo)
mapa_real = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 5), ('E', 2)],
    'C': [('F', 3)],
    'D': [('G', 1)],
    'E': [('G', 6)],
    'F': [('G', 1)]
}

# Heurística h(n) (estimación al objetivo 'G')
h_n = {'A': 7, 'B': 6, 'C': 2, 'D': 1, 'E': 4, 'F': 1, 'G': 0}

ruta, costo_final = busqueda_a_estrella(mapa_real, 'A', 'G', h_n)

if ruta:
    print(f"\nRuta óptima A*: {' -> '.join(ruta)}")
    print(f"Costo real total: {costo_final}")
