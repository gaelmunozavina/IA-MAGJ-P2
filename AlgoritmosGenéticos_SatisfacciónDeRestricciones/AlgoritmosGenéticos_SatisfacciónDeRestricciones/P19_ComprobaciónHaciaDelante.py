def forward_checking(variable, valor, dominios, vecinos):
    """
    Reduce los dominios de los vecinos de la variable actual.
    Retorna False si algún dominio se queda vacío.
    """
    nuevos_dominios = {v: list(d) for v, d in dominios.items()}
    
    for vecino in vecinos.get(variable, []):
        if valor in nuevos_dominios[vecino]:
            nuevos_dominios[vecino].remove(valor)
            # Si un vecino se queda sin opciones, esta rama no sirve
            if not nuevos_dominios[vecino]:
                return None
    return nuevos_dominios

def resolver_csp_fc(variables, dominios, vecinos, asignacion={}):
    """Backtracking mejorado con Forward Checking."""
    if len(asignacion) == len(variables):
        return asignacion

    # Seleccionar variable no asignada
    var = [v for v in variables if v not in asignacion][0]

    for valor in dominios[var]:
        # Verificamos si el valor es consistente (FC hace gran parte de esto)
        print(f"Probando {var} = {valor}")
        
        # Aplicamos Forward Checking
        dominios_reducidos = forward_checking(var, valor, dominios, vecinos)
        
        if dominios_reducidos is not None:
            asignacion[var] = valor
            resultado = resolver_csp_fc(variables, dominios_reducidos, vecinos, asignacion)
            
            if resultado:
                return resultado
            
            # Backtrack
            del asignacion[var]

    return None

# --- CONFIGURACIÓN ---
vars_mapa = ['A', 'B', 'C']
doms_iniciales = {v: ['Rojo', 'Verde'] for v in vars_mapa}
# A y B son vecinos, B y C son vecinos
vecinos_mapa = {'A': ['B'], 'B': ['A', 'C'], 'C': ['B']}

solucion = resolver_csp_fc(vars_mapa, doms_iniciales, vecinos_mapa)

print(f"\nResultado final: {solucion}")
