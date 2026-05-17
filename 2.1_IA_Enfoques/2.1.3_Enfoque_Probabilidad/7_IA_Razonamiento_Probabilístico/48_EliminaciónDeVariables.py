class Factor:
    def __init__(self, variables, valores):
        self.vars = variables  # Ej: ['A', 'B']
        self.data = valores    # Diccionario con combinaciones

    def eliminar_variable(self, var):
        """Marginalización: Sumar sobre una variable para eliminarla."""
        nuevas_vars = [v for v in self.vars if v != var]
        nuevos_valores = {}
        
        for combinacion, prob in self.data.items():
            # Crear nueva clave sin la variable eliminada
            nueva_comb = tuple(v for i, v in enumerate(combinacion) if self.vars[i] != var)
            nuevos_valores[nueva_comb] = nuevos_valores.get(nueva_comb, 0) + prob
            
        return Factor(nuevas_vars, nuevos_valores)

# --- EJEMPLO ---
# P(A)
f1 = Factor(['A'], {(True,): 0.2, (False,): 0.8})

# P(B|A) - Simplificado como factor conjunto P(A, B)
f2 = Factor(['A', 'B'], {
    (True, True): 0.18,   # P(A)*P(B|A)
    (True, False): 0.02,
    (False, True): 0.32,
    (False, False): 0.48
})

# Eliminamos 'A' para quedarnos solo con la probabilidad marginal de B
f_solo_b = f2.eliminar_variable('A')

print("Factor resultante para B tras eliminar A (Marginalización):")
for comb, prob in f_solo_b.data.items():
    print(f"  P(B={comb[0]}): {prob:.2f}")
