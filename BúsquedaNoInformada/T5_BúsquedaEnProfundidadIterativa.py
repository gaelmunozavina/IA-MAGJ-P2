def dls_para_ids(grafo, nodo, meta, limite):
    """
    Función auxiliar: Realiza una Búsqueda en Profundidad Limitada (DLS).
    
    Esta función es el motor de la búsqueda iterativa. Explora hasta
    un nivel específico y se detiene.
    """
    # Si el nodo actual es el que buscamos, devolvemos el camino con el nodo
    if nodo == meta:
        return [nodo]
    
    # Si el límite llega a 0, dejamos de explorar esta rama
    if limite <= 0:
        return None
    
    # Exploramos los hijos/vecinos del nodo actual
    for vecino in grafo.get(nodo, []):
        # Llamada recursiva restando 1 al límite de profundidad
        camino = dls_para_ids(grafo, vecino, meta, limite - 1)
        
        # Si la meta fue encontrada en niveles inferiores, reconstruimos la ruta
        if camino is not None:
            return [nodo] + camino
            
    return None

def busqueda_profundidad_iterativa(grafo, inicio, meta, max_limite):
    """
    Ejecuta la Búsqueda en Profundidad Iterativa (IDS).
    
    Llama a la función DLS repetidamente, aumentando el límite de 
    profundidad en cada paso (0, 1, 2...).
    """
    # El bucle 'for' controla hasta qué profundidad vamos a intentar buscar
    for limite in range(max_limite + 1):
        print(f"Probando con límite de profundidad: {limite}")
        
        # Intentamos encontrar la meta con el límite actual
        resultado = dls_para_ids(grafo, inicio, meta, limite)
        
        # Si el resultado no es None, significa que encontramos la ruta óptima
        if resultado is not None:
            print(f"¡Meta encontrada en el nivel {limite}!")
            return resultado
            
    # Si termina el bucle sin retornar, la meta no estaba al alcance
    return None

# --- EJEMPLO DE PRUEBA ---
# Representación de un árbol de búsqueda simple
grafo_universidad = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [], 
    'E': [], 
    'F': [], 
    'G': []
}

# Configuración de la búsqueda
inicio_nodo = 'A'
objetivo_nodo = 'G'
maximo_a_probar = 5 # Límite máximo de seguridad para evitar bucles infinitos

# Ejecución del algoritmo
ruta_final = busqueda_profundidad_iterativa(grafo_universidad, inicio_nodo, objetivo_nodo, maximo_a_probar)

# Presentación de resultados
if ruta_final:
    print(f"\nRuta óptima encontrada: {' -> '.join(ruta_final)}")
else:
    print("\nNo se encontró la meta en el rango de profundidad permitido.")
