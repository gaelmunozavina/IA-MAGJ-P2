from collections import deque

def bfs(grafo, inicio)
    
    Realiza una búsqueda en anchura (BFS) en un grafo.
    
    Args
        grafo (dict) Representación del grafo (lista de adyacencia).
        inicio El nodo desde donde empieza la búsqueda.
    
    # 1. Crear una cola y agregar el nodo inicial
    cola = deque([inicio])
    
    # 2. Mantener un registro de los nodos visitados para evitar ciclos
    visitados = {inicio}
    
    print(fIniciando búsqueda desde el nodo {inicio})

    while cola
        # Sacar el primer nodo que entró a la cola (FIFO)
        nodo_actual = cola.popleft()
        print(fVisitando nodo {nodo_actual})

        # Explorar los vecinos del nodo actual
        for vecino in grafo[nodo_actual]
            if vecino not in visitados
                # Si el vecino no se ha visitado, se marca y se encola
                visitados.add(vecino)
                cola.append(vecino)

# --- Ejemplo de uso ---

# Representamos un grafo pequeño
# A se conecta con B y C
# B se conecta con D y E
# C se conecta con F
grafo_ejemplo = {
    'A' ['B', 'C'],
    'B' ['A', 'D', 'E'],
    'C' ['A', 'F'],
    'D' ['B'],
    'E' ['B', 'F'],
    'F' ['C', 'E']
}

# Llamamos a la función
bfs(grafo_ejemplo, 'A')