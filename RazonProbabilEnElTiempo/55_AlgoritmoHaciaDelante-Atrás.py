import numpy as np

# Parámetros del modelo
T = np.array([[0.7, 0.3], [0.3, 0.7]]) # Transición (Sol, Lluvia)
O = np.array([[0.1, 0.9], [0.8, 0.2]]) # Emisión (Paraguas: Sí, No)
prior = np.array([0.5, 0.5])

def forward_backward(evidencias):
    t_max = len(evidencias)
    
    # 1. Paso Forward (Filtrado)
    f = [prior]
    for i in range(t_max):
        # Predicción * Observación
        f_next = (f[-1] @ T) * O[:, evidencias[i]]
        f.append(f_next / sum(f_next)) # Normalizar
        
    # 2. Paso Backward (Mensajes hacia atrás)
    b = [np.array([1.0, 1.0])] # Inicializar al final
    for i in range(t_max - 1, -1, -1):
        # Transición * Observación * b_next
        b_prev = T @ (O[:, evidencias[i]] * b[0])
        b.insert(0, b_prev) # No normalizar usualmente hasta el final
        
    # 3. Combinación (Suavizado)
    suavizado = []
    for i in range(len(f)):
        res = f[i] * b[i]
        suavizado.append(res / sum(res))
        
    return suavizado

# --- ESCENARIO ---
# Evidencias (Paraguas): [Sí, Sí, No] -> Codificado como [0, 0, 1]
obs = [0, 0, 1]
probabilidades_suavizadas = forward_backward(obs)

print("Probabilidades suavizadas (Estado Lluvioso):")
for t, prob in enumerate(probabilidades_suavizadas):
    print(f"  Tiempo {t}: {prob[1]:.4f}")
  
