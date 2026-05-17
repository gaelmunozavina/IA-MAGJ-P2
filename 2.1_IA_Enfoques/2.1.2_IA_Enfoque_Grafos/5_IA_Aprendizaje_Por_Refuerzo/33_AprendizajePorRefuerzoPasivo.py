class AprendizajePasivoTD:
    def __init__(self, estados, alpha=0.1, gamma=0.9):
        self.V = {s: 0 for s in estados} # Utilidades estimadas
        self.alpha = alpha               # Tasa de aprendizaje
        self.gamma = gamma               # Factor de descuento

    def actualizar(self, s, r, s_sig):
        """
        Regla de actualización TD:
        V(s) = V(s) + alpha * (R(s) + gamma * V(s_sig) - V(s))
        """
        error_prediccion = r + self.gamma * self.V[s_sig] - self.V[s]
        self.V[s] += self.alpha * error_prediccion
        return error_prediccion

# --- SIMULACIÓN DE EXPERIENCIA ---
# El agente sigue una ruta fija: A -> B -> Meta
estados_mundo = ['A', 'B', 'Meta']
agente_td = AprendizajePasivoTD(estados_mundo)

# Simulamos 100 veces el recorrido para que aprenda
for episodio in range(100):
    # Paso 1: De A a B (recompensa pequeña negativa por "vivir")
    agente_td.actualizar('A', -0.1, 'B')
    # Paso 2: De B a Meta (recompensa grande positiva)
    agente_td.actualizar('B', 10.0, 'Meta')

print("Utilidades aprendidas mediante Diferencia Temporal (TD):")
for estado, valor in agente_td.V.items():
    print(f"  Estado {estado}: {valor:.4f}")
