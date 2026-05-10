from collections import deque

def ac3(variables, dominios, restricciones):
    """
    Algoritmo AC-3 para asegurar consistencia de arco.
    
    Args:
        variables: Lista de variables.
        dominios: Diccionario {var: [valores]}.
        restricciones: Diccionario {var: [(vecino, func_validacion)]}.
    """
    # Inicializar la cola con todos los arcos (pares de variables relacionadas)
    cola = deque()
    for v1 in restricciones:
        for v2, func in restricciones[v1]:
            cola.append((v1, v2, func))

    print(f"Iniciando AC-3 con {len(cola)} arcos en la cola...")

    while cola:
        xi, xj, func = cola.popleft()
        
        if revisar(xi, xj, func, dominios):
            # Si el dominio de xi quedó vacío, el problema no tiene solución
            if not dominios[xi]:
                return False
            
            # Si el dominio cambió, debemos volver a revisar a los vecinos de xi
            for vecino, f_vec in restricciones.get(xi, []):
                if vecino != xj:
                    cola.append((vecino, xi, f_vec))
                    
    return True

def revisar(xi, xj, func, dominios):
    """Revisa si cada valor en el dominio de xi tiene un compañero en xj."""
    revisado = False
    for valor_i in dominios[xi][:]:
        # ¿Existe algún valor en el dominio de xj que cumpla la restricción?
        if not any(func(valor_i, valor_j) for valor_j in dominios[xj]):
            dominios[xi].remove(valor_i)
            revisado = True
    return revisado

# --- PRUEBA CON UN SUDOKU MINI O COLOREO ---
vars_csp = ['X', 'Y', 'Z']
doms_csp = {
    'X': [1, 2],
    'Y': [1, 2],
    'Z': [1]
}

# Restricción: X != Y, Y != Z, X != Z
def distinto(a, b): return a != b

restrs_csp = {
    'X': [('Y', distinto), ('Z', distinto)],
    'Y': [('X', distinto), ('Z', distinto)],
    'Z': [('X', distinto), ('Y', distinto)]
}

if ac3(vars_csp, doms_csp, restrs_csp):
    print("\nDominios después de la Propagación (AC-3):")
    for v, d in doms_csp.items():
        print(f"  Variable {v}: {d}")
else:
    print("\nEl problema es inconsistente.")
