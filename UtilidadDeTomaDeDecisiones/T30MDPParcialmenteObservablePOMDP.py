class POMDP_Agente:
    def __init__(self, estados, creencias_iniciales, modelo_obs):
        self.estados = estados
        self.creencias = creencias_iniciales  # Distribución de prob. inicial
        self.modelo_obs = modelo_obs          # P(obs | estado)

    def actualizar_creencia(self, accion, observacion, transiciones):
        """Actualiza el estado de creencia usando Bayes."""
        nueva_creencia = {}
        
        for s_sig in self.estados:
            # 1. Predicción: ¿Cuál es la prob. de estar en s_sig dado la acción?
            prob_predicha = sum(self.creencias[s] * transiciones[s][accion].get(s_sig, 0) 
                               for s in self.estados)
            
            # 2. Corrección: Ajustar con la observación recibida
            prob_obs = self.modelo_obs[s_sig].get(observacion, 0)
            nueva_creencia[s_sig] = prob_obs * prob_predicha

        # 3. Normalización: Asegurar que la suma de probabilidades sea 1
        total = sum(nueva_creencia.values())
        self.creencias = {s: p / total for s, p in nueva_creencia.items()}
        return self.creencias

# --- CONFIGURACIÓN ---
estados = ['Celda_1', 'Celda_2', 'Celda_3']
creencias = {'Celda_1': 0.33, 'Celda_2': 0.33, 'Celda_3': 0.34}

# El sensor dice "Muro" con 90% de prob si estás en la Celda_1
modelo_sensor = {
    'Celda_1': {'Muro': 0.9, 'Vacio': 0.1},
    'Celda_2': {'Muro': 0.1, 'Vacio': 0.9},
    'Celda_3': {'Muro': 0.1, 'Vacio': 0.9}
}

trans = {s: {'Mover': {s: 1.0}} for s in estados} # Simplificado: no se mueve

agente = POMDP_Agente(estados, creencias, modelo_sensor)

# El agente recibe la observación "Muro"
nuevas_creencias = agente.actualizar_creencia('Mover', 'Muro', trans)

print("Actualización de Creencia (Belief State) tras observar 'Muro':")
for s, p in nuevas_creencias.items():
    print(f"  P({s}): {p:.4f}")
  
