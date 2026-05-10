def resolver_por_acondicionamiento(variables, dominios, restricciones, cutset):
    """
    Simulación de resolución de CSP usando Acondicionamiento del Corte.
    """
    # 1. Separar variables del árbol
    vars_arbol = [v for v in variables if v not in cutset]
    
    print(f"Variables de corte (Cutset): {cutset}")
    print(f"Variables restantes (Estructura de árbol): {vars_arbol}")

    # 2. Probar asignaciones para el cutset (Simplificado a una sola prueba)
    asignacion_cutset = {}
    for v in cutset:
        asignacion_cutset[v] = dominios[v][0] # Tomamos el primer valor disponible
    
    print(f"Asignación fija del cutset: {asignacion_cutset}")

    # 3. Pre-procesamiento: Eliminar valores inconsistentes en el árbol
    dominios_reducidos = {v: list(d) for v, d in dominios.items() if v in vars_arbol}
    
    for v_corte, valor_corte in asignacion_cutset.items():
        for v_arbol in vars_arbol:
            # Si hay una restricción entre la variable de corte y la del árbol
            if (v_corte, v_arbol) in restricciones:
                func = restricciones[(v_corte, v_arbol)]
                dominios_reducidos[v_arbol] = [
                    val for val in dominios_reducidos[v_arbol] 
                    if func(valor_corte, val)
                ]

    # 4. Verificar si el árbol sigue siendo viable
    for v in vars_arbol:
        if not dominios_reducidos[v]:
            print(f"Fallo: El dominio de {v} quedó vacío tras el acondicionamiento.")
            return None

    print("El árbol resultante es consistente. Se puede resolver en tiempo lineal.")
    return {**asignacion_cutset, **{v: d[0] for v, d in dominios_reducidos.items()}}

# --- CONFIGURACIÓN ---
variables = ['A', 'B', 'C', 'D']
# Supongamos un ciclo A-B-C-A y D conectado a C
dominios = {v: [1, 2] for v in variables}
restricciones = {
    ('A', 'B'): lambda a, b: a != b,
    ('B', 'C'): lambda b, c: b != c,
    ('C', 'A'): lambda c, a: c != a,
    ('C', 'D'): lambda c, d: c != d
}

# Si quitamos 'C', el ciclo A-B-C-A se rompe y queda un árbol
sol = resolver_por_acondicionamiento(variables, dominios, restricciones, cutset=['C'])
print(f"Solución encontrada: {sol}")
