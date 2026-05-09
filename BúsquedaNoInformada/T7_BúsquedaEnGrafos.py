def busqueda_general_grafos(grafo, inicio, meta):
    """
    Plantilla general para búsqueda en grafos con control de nodos visitados.
    
    Args:
        grafo: Diccionario de adyacencia.
        inicio: Nodo inicial.
        meta: Nodo objetivo.
    """
    # 1. La Frontera: Nodos por explorar (usamos una lista como ejemplo simple)
    frontera = [[inicio]]
    
    # 2. Conjunto de Explorados: Evita ciclos y repeticiones (Memoria)
    explorados = set()

    print(f"Iniciando búsqueda de {inicio} a {meta}...")

    while frontera:
        # Extraemos el primer camino de la frontera
        camino = frontera.pop(0)
        nodo_actual = camino[-1]

        # Si ya visitamos este nodo, lo ignoramos y seguimos con el siguiente
        if nodo_actual in explorados:
            continue

        # Si es la meta, ¡éxito!
        if nodo_actual == meta:
            return camino

        # Marcar como explorado
        explorados.add(nodo_actual)
        print(f"  Nodo {nodo_actual} explorado. Memoria actual: {explorados}")

        # Expandir vecinos
        for vecino in grafo.get(nodo_actual, []):
            if vecino not in explorados:
                nuevo_camino = list(camino)
                nuevo_camino.append(vecino)
                frontera.append(nuevo_camino)

    return None

# --- EJEMPLO DE PRUEBA CON CICLO ---
# A -> B -> C -> A (Un ciclo infinito potencial)
grafo_con_ciclos = {
    'A': ['B'],
    'B': ['C'],
    'C': ['A', 'D'],
    'D': []
}

ruta = busqueda_general_grafos(grafo_con_ciclos, 'A', 'D')

if ruta:
    print(f"\nResultado: Ruta encontrada -> {' -> '.join(ruta)}")
else:
    print("\nNo se encontró una ruta.")
