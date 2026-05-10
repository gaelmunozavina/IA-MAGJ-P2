def es_seguro(tablero, fila, col, n):
    """Verifica si es seguro colocar una reina en tablero[fila][col]."""
    # Verificar fila hacia la izquierda
    for i in range(col):
        if tablero[fila][i] == 1:
            return False

    # Verificar diagonal superior izquierda
    for i, j in zip(range(fila, -1, -1), range(col, -1, -1)):
        if tablero[i][j] == 1:
            return False

    # Verificar diagonal inferior izquierda
    for i, j in zip(range(fila, n, 1), range(col, -1, -1)):
        if tablero[i][j] == 1:
            return False

    return True

def resolver_n_reinas(tablero, col, n):
    """Algoritmo de Backtracking para colocar las reinas."""
    # Caso base: Si todas las reinas están colocadas
    if col >= n:
        return True

    # Intentar colocar la reina en cada fila de esta columna
    for i in range(n):
        if es_seguro(tablero, i, col, n):
            tablero[i][col] = 1 # Colocar reina

            # Recursión para colocar el resto
            if resolver_n_reinas(tablero, col + 1, n):
                return True

            # Si colocar la reina aquí no lleva a una solución, BACKTRACK
            tablero[i][col] = 0 

    return False

# --- CONFIGURACIÓN ---
N = 4
tablero_n = [[0 for _ in range(N)] for _ in range(N)]

if resolver_n_reinas(tablero_n, 0, N):
    print(f"--- Solución para {N} Reinas ---")
    for fila in tablero_n:
        print(fila)
else:
    print("No existe solución.")
