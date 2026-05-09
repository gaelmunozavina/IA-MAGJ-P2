import math

def heuristica_manhattan(actual, meta):
    """
    Calcula la distancia de Manhattan entre dos puntos (x1, y1) y (x2, y2).
    Ideal para movimientos en cuadrículas donde no puedes moverte en diagonal.
    """
    x1, y1 = actual
    x2, y2 = meta
    return abs(x1 - x2) + abs(y1 - y2)

def heuristica_euclidiana(actual, meta):
    """
    Calcula la distancia en línea recta (teorema de Pitágoras).
    Ideal para mapas abiertos o navegación aérea.
    """
    x1, y1 = actual
    x2, y2 = meta
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# --- EJEMPLO DE USO ---

posicion_robot = (0, 0)
posicion_meta = (5, 3)

h_m = heuristica_manhattan(posicion_robot, posicion_meta)
h_e = heuristica_euclidiana(posicion_robot, posicion_meta)

print(f"Punto actual: {posicion_robot} | Meta: {posicion_meta}")
print(f"Estimación Manhattan: {h_m} pasos.")
print(f"Estimación Euclidiana: {h_e:.2f} unidades.")
