def dfs_recursivo(grafo, nodo, visitados=None):
    """
    Realiza una búsqueda en profundidad (DFS) de forma recursiva.
    
    Args:
        grafo: Diccionario de adyacencia.
        nodo: Nodo actual siendo explorado.
        visitados: Conjunto de nodos que ya pasaron por el proceso.
    """
    if visitados is None:
        visitados = set()

    # Marcamos el nodo actual como visitado
    visitados.add(nodo)
    print(f"Visitando nodo: {nodo}")

    # Exploramos cada vecino a fondo antes de pasar al siguiente
    for vecino in grafo.get(nodo, []):
        if vecino not in visitados:
            # Llamada recursiva: vamos más profundo por esta rama
            dfs_recursivo(grafo, vecino, visitados)

# --- EJEMPLO DE USO ---
# Usamos el mismo grafo para comparar resultados con BFS
grafo_estudio = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("Orden de exploración DFS:")
dfs_recursivo(grafo_estudio, 'A')
