import numpy as np

# Modelo: P(X_t | X_{t-1}) -> Matriz de Transición
# 0: Funcionando, 1: Fallo
T = np.array([
    [0.9, 0.1], # Si funciona, 90% sigue funcionando
    [0.3, 0.7]  # Si falló, 30% se recupera solo
])

# Modelo de Sensor: P(E_t | X_t) -> Matriz de Emisión
# Sensor dice "Luz Verde" (0) o "Luz Roja" (1)
# Si funciona (0), luz verde 95% veces. Si falla (1), luz roja 80% veces.
O = np.array([
    [0.95, 0.05], # Estado 0
    [0.20, 0.80]  # Estado 1
])

def filtrar(creencia_anterior, evidencia):
    # 1. Paso de Predicción (Ecuación de Chapman-Kolmogorov)
    prediccion = creencia_anterior @ T
    
    # 2. Paso de Actualización (Bayes)
    # Multiplicar por la probabilidad de la evidencia observada
    filtrado = prediccion * O[:, evidencia]
    
    # Normalizar
    return filtrado / sum(filtrado)

# --- ESCENARIO ---
creencia_inicial = np.array([0.5, 0.5]) # No sabemos nada al inicio
evidencia_hoy = 1 # El sensor marca LUZ ROJA

# Ejecutar Filtrado
hoy = filtrar(creencia_inicial, evidencia_hoy)
# Ejecutar Predicción para mañana (sin ver nueva evidencia)
manana = hoy @ T

print(f"Evidencia recibida: LUZ ROJA")
print(f"Filtrado (Estado Actual): Funciona: {hoy[0]:.2f}, Fallo: {hoy[1]:.2f}")
print(f"Predicción (Estado Mañana): Funciona: {manana[0]:.2f}, Fallo: {manana[1]:.2f}")
