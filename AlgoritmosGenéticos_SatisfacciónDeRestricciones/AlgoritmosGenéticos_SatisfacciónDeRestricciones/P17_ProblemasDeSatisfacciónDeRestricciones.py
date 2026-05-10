class CSP:
    def __init__(self, variables, dominios, restricciones):
        self.variables = variables
        self.dominios = dominios
        self.restricciones = restricciones # Función que valida la regla

    def es_consistente(self, variable, asignacion, valor):
        """Verifica si asignar un valor a una variable rompe alguna regla."""
        for variable_vecina, restriccion_func in self.restricciones.get(variable, []):
            if variable_vecina in asignacion and not restriccion_func(valor, asignacion[variable_vecina]):
                return False
        return True

    def backtracking(self, asignacion={}):
        """Algoritmo de búsqueda con retroceso para resolver el CSP."""
        # Si todas las variables tienen valor, terminamos
        if len(asignacion) == len(self.variables):
            return asignacion

        # Seleccionar la siguiente variable sin asignar
        variable = [v for v in self.variables if v not in asignacion][0]

        for valor in self.dominios[variable]:
            if self.es_consistente(variable, asignacion, valor):
                asignacion[variable] = valor
                
                # Llamada recursiva
                resultado = self.backtracking(asignacion)
                if resultado is not None:
                    return resultado
                
                # Si falló, retrocedemos (Backtrack)
                del asignacion[variable]

        return None

# --- EJEMPLO: COLOREO DE MAPA ---
# Queremos colorear 3 regiones (A, B, C) donde A es vecina de B y B de C.
vars = ['A', 'B', 'C']
doms = {v: ['Rojo', 'Verde', 'Azul'] for v in vars}

# Restricción: los valores deben ser distintos
def distintos(v1, v2):
    return v1 != v2

restrs = {
    'A': [('B', distintos)],
    'B': [('A', distintos), ('C', distintos)],
    'C': [('B', distintos)]
}

# Ejecución
problema = CSP(vars, doms, restrs)
solucion = problema.backtracking()

print("--- Solución al problema de coloreo ---")
if solucion:
    for var, color in solucion.items():
        print(f"Región {var}: {color}")
else:
    print("No existe solución.")
