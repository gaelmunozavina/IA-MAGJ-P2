import random

def contar_conflictos(variable, valor, asignacion, restricciones):
    """Cuenta cuántas restricciones se rompen si asignamos 'valor' a 'variable'."""
    conflictos = 0
    for vecino in restricciones.get(variable, []):
        if vecino in asignacion and asignacion[vecino] == valor:
            conflictos += 1
    return conflictos

def min_conflicts(variables, dominios, restricciones, max_pasos=100):
    """
    Algoritmo de búsqueda local de Mínimos-Conflictos.
    """
    # 1. Asignación inicial completa (aleatoria)
    asignacion = {v: random.choice(dominios[v]) for v in variables}
    
    for i in range(max_pasos):
        # Encontrar variables que tienen conflictos
        con_conflictos = [v for v in variables if contar_conflictos(v, asignacion[v], asignacion, restricciones) > 0]
        
        # Si no hay conflictos, ¡hemos terminado!
        if not con_conflictos:
            print(f"Solución encontrada en {i} pasos.")
            return asignacion
        
        # 2. Elegir una variable conflictiva al azar
        var = random.choice(con_conflictos)
        
        # 3. Elegir el valor que minimice los conflictos
        # Si hay empate, se elige uno al azar entre los mejores
        mejor_valor = asignacion[var]
        min_c = contar_conflictos(var, mejor_valor, asignacion, restricciones)
        
        valores_posibles = list(dominios[var])
        random.shuffle(valores_posibles)
        
        for valor in valores_posibles:
            c = contar_conflictos(var, valor, asignacion, restricciones)
            if c < min_c:
                min_c = c
                mejor_valor = valor
        
        asignacion[var] = mejor_valor
        
    return None # Fallo al no encontrar solución en los pasos dados

# --- EJEMPLO DE PRUEBA ---
vars_list = ['A', 'B', 'C', 'D', 'E']
doms_dict = {v: [1, 2, 3] for v in vars_list}
# Restricciones: todos los conectados deben ser diferentes
restrs_dict = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'E'],
    'D': ['B'],
    'E': ['C']
}

solucion = min_conflicts(vars_list, doms_dict, restrs_dict)

if solucion:
    print(f"Configuración final: {solucion}")
else:
    print("No se encontró solución en el tiempo límite.")
