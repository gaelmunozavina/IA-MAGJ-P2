def dls_recursivo(grafo, nodo, meta, limite, profundidad_actual=0):
    """
    Realiza una Búsqueda en Profundidad Limitada (DLS).
    
    Args:
        grafo: Diccionario de adyacencia.
        nodo: Nodo actual.
        meta: Nodo objetivo.
        limite: Profundidad máxima permitida.
        profundidad_actual: Nivel actual de la búsqueda.
    """
    print(f"Explorando nodo: {nodo} en profundidad {profundidad_actual}")

    # Caso 1: Encontramos la meta
    if nodo == meta:
        return [nodo]

    # Caso 2: Llegamos al límite de profundidad sin encontrar la meta
    if profundidad_actual >= limite:
        return None

    # Caso 3: Explorar vecinos (siempre que estemos bajo el límite)
    for vecino in grafo.get(nodo, []):
        resultado = dls_recursivo(grafo, vecino, meta, limite, profundidad_actual + 1)
        if resultado is not None:
            # Si se encontró la meta en una rama hija, reconstruimos el camino
            return [nodo] + resultado

    return None

# --- EJEMPLO DE PRUEBA ---
mapa_ia = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': ['G'],
    'G': []
}

inicio = 'A'
objetivo = 'G'
limite_max = 2  # G está en profundidad 3, así que con límite 2 no debería encontrarlo

print(f"--- Buscando a {objetivo} con límite {limite_max} ---")
camino = dls_recursivo(mapa_ia, inicio, objetivo, limite_max)

if camino:
    print(f"\n¡Meta encontrada! Ruta: {' -> '.join(camino)}")
else:
    print(f"\nNo se encontró el objetivo dentro del límite de profundidad {limite_max}.")
