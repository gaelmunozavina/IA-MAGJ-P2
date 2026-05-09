import random

def funcion_objetivo(x):
    """Función de evaluación: queremos encontrar el pico más alto."""
    return -(x - 2)**2 + 15

def obtener_vecinos(x, paso=0.5):
    """Genera dos vecinos cercanos para un estado dado."""
    return [x - paso, x + paso]

def local_beam_search(k, iteraciones):
    """
    Algoritmo de Búsqueda de Haz Local.
    
    Args:
        k: Número de estados (haces) que mantendremos activos.
        iteraciones: Número de pasos de búsqueda.
    """
    # 1. Generar k estados iniciales aleatorios
    haces = [random.uniform(-10, 10) for _ in range(k)]
    
    print(f"Iniciando con {k} estados aleatorios: {[round(h, 2) for h in haces]}")

    for i in range(iteraciones):
        todos_los_vecinos = []
        
        # 2. Generar vecinos para todos los estados actuales
        for estado in haces:
            todos_los_vecinos.extend(obtener_vecinos(estado))
        
        # Incluimos los estados actuales para no perderlos si son mejores que los vecinos
        todos_los_vecinos.extend(haces)
        
        # 3. Evaluar y seleccionar los k mejores
        # Ordenamos por el valor de la función objetivo de mayor a menor
        todos_los_vecinos.sort(key=lambda x: funcion_objetivo(x), reverse=True)
        haces = todos_los_vecinos[:k]
        
        if i % 2 == 0:
            mejor_actual = funcion_objetivo(haces[0])
            print(f"Iteración {i}: Mejor valor encontrado = {mejor_actual:.4f}")

    return haces[0], funcion_objetivo(haces[0])

# --- EJECUCIÓN ---
# k=3: mantenemos 3 caminos activos simultáneamente
mejor_x, mejor_val = local_beam_search(k=3, iteraciones=10)

print(f"\nResultado Final:")
print(f"Mejor estado (x): {mejor_x:.4f}")
print(f"Valor máximo: {mejor_val:.4f}")
