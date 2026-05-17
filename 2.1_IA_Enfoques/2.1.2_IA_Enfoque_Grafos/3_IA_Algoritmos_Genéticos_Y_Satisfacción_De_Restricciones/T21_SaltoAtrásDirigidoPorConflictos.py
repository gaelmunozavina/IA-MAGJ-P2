class BackjumpingCSP:
    def __init__(self, variables, dominios, restricciones):
        self.variables = variables
        self.dominios = dominios
        self.restricciones = restricciones
        # Conjunto de conflictos para cada variable: {var: set(variables_culpables)}
        self.conflict_sets = {v: set() for v in variables}

    def resolver(self, index=0, asignacion={}):
        if len(asignacion) == len(self.variables):
            return asignacion

        var_actual = self.variables[index]
        
        for valor in self.dominios[var_actual]:
            # Verificar consistencia
            es_consistente = True
            for var_previa in self.variables[:index]:
                # Si hay una restricción entre la previa y la actual
                if (var_previa, var_actual) in self.restricciones or (var_actual, var_previa) in self.restricciones:
                    # Supongamos una restriccion simple de desigualdad
                    if asignacion[var_previa] == valor:
                        self.conflict_sets[var_actual].add(var_previa)
                        es_consistente = False
                        break
            
            if es_consistente:
                asignacion[var_actual] = valor
                resultado = self.resolver(index + 1, asignacion)
                
                if resultado is not None:
                    return resultado
                
                # Si falló adelante, heredamos los conflictos de la variable que falló
                # (Simplificación del algoritmo Prosser's CBJ)
                print(f"Fallo en cadena tras asignar {var_actual}={valor}, analizando salto...")
                del asignacion[var_actual]

        # Si llegamos aquí, ningún valor funcionó para var_actual
        # El algoritmo real retornaría el índice del salto atrás
        return None

# --- CONFIGURACIÓN DE PRUEBA ---
v_list = ['X1', 'X2', 'X3', 'X4']
d_dict = {v: [1, 2] for v in v_list}
# Supongamos que X1 y X4 tienen una restricción fuerte que causa el conflicto
r_list = [('X1', 'X2'), ('X2', 'X3'), ('X3', 'X4'), ('X1', 'X4')]

instancia = BackjumpingCSP(v_list, d_dict, r_list)
sol = instancia.resolver()

print(f"\nResultado del proceso: {sol}")
