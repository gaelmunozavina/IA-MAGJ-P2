# Simulación de un diccionario de uniones válidas (Simplificado)
# Representamos las etiquetas como: 1 (Convexa), -1 (Cóncava), 0 (Oclusión)
uniones_y_validas = [
    (1, 1, 1),    # Esquina exterior de un cubo
    (-1, -1, -1), # Esquina interior de una caja
    (0, 0, 1)     # (Ejemplo de otra configuración válida)
]

def verificar_union_y(etiquetas):
    if etiquetas in uniones_y_validas:
        return "Configuración físicamente posible."
    else:
        return "Configuración IMPOSIBLE (Objeto de Escher)."

# --- ESCENARIO ---
# Intentamos etiquetar una unión en Y donde las 3 aristas son convexas (+)
print(f"Probando unión (1, 1, 1): {verificar_union_y((1, 1, 1))}")

# Intentamos una combinación que no existe en el mundo físico
print(f"Probando unión (1, -1, 0): {verificar_union_y((1, -1, 0))}")
