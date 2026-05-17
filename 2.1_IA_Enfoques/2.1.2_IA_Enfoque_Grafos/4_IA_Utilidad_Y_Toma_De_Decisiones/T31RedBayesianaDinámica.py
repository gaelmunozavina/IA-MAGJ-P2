class RedBayesianaDinamica:
    def __init__(self):
        # Probabilidad inicial: P(Salud_0 = Buena) = 0.9
        self.creencia_actual = 0.9 
        
        # Modelo de Transición: P(Salud_t+1 | Salud_t)
        # Si está buena, 80% sigue buena. Si está mal, 100% sigue mal (falla persistente).
        self.transicion = {True: 0.8, False: 0.0}
        
        # Modelo de Sensor: P(Lectura = OK | Salud)
        # Si está buena, el sensor acierta 90%. Si está mal, el sensor da error 80%.
        self.sensor = {True: 0.9, False: 0.2}

    def filtrar(self, lectura_ok):
        """Paso de filtrado: Estimar el estado actual dada una nueva observación."""
        
        # 1. Predicción (Paso de tiempo t -> t+1)
        # P(S_1) = P(S_1|S_0)*P(S_0) + P(S_1|not S_0)*P(not S_0)
        p_buena_predicha = (self.creencia_actual * self.transicion[True]) + \
                           ((1 - self.creencia_actual) * self.transicion[False])
        
        # 2. Actualización (Incorporar evidencia del sensor)
        # Usamos Bayes: P(S|E) = alpha * P(E|S) * P(S)
        prob_obs = self.sensor[True] if lectura_ok else (1 - self.sensor[True])
        prob_obs_si_falla = self.sensor[False] if lectura_ok else (1 - self.sensor[False])
        
        buena_final = prob_obs * p_buena_predicha
        mala_final = prob_obs_si_falla * (1 - p_buena_predicha)
        
        # Normalización
        self.creencia_actual = buena_final / (buena_final + mala_final)
        return self.creencia_actual

# --- SIMULACIÓN ---
dbn = RedBayesianaDinamica()
lecturas = [True, True, False] # El sensor reporta OK, OK, y luego un ERROR

print(f"Creencia inicial (Salud Buena): 90%")
for i, obs in enumerate(lecturas, 1):
    prob = dbn.filtrar(obs)
    print(f"Paso {i} (Lectura={'OK' if obs else 'ERROR'}): Confianza en salud buena = {prob:.4f}")
  
