import numpy as np

class HMM:
    def __init__(self):
        # Estados: 0: Feliz, 1: Triste
        self.estados = ["Feliz", "Triste"]
        # Observaciones: 0: Canta, 1: Habla, 2: Silencio
        self.observaciones = ["Canta", "Habla", "Silencio"]
        
        # P(X_t | X_{t-1}) - Matriz de Transición
        self.T = np.array([
            [0.8, 0.2], # Feliz -> Feliz (0.8), Feliz -> Triste (0.2)
            [0.3, 0.7]  # Triste -> Feliz (0.3), Triste -> Triste (0.7)
        ])
        
        # P(E_t | X_t) - Matriz de Emisión
        self.O = np.array([
            [0.6, 0.3, 0.1], # Feliz: Canta(60%), Habla(30%), Silencio(10%)
            [0.1, 0.4, 0.5]  # Triste: Canta(10%), Habla(40%), Silencio(50%)
        ])
        
        self.prior = np.array([0.5, 0.5])

    def filtrar(self, secuencia_obs):
        creencia = self.prior
        for obs_idx in secuencia_obs:
            # 1. Predicción (Hacia adelante)
            prediccion = creencia @ self.T
            # 2. Actualización (Evidencia)
            creencia = prediccion * self.O[:, obs_idx]
            # Normalizar
            creencia /= creencia.sum()
        return creencia

# --- PRUEBA ---
modelo = HMM()
# Vemos a alguien: Habla -> En Silencio -> En Silencio
secuencia = [1, 2, 2] 
prob_final = modelo.filtrar(secuencia)

print(f"Tras observar { [modelo.observaciones[i] for i in secuencia] }:")
print(f"Probabilidad de estar Feliz: {prob_final[0]:.4f}")
print(f"Probabilidad de estar Triste: {prob_final[1]:.4f}")
